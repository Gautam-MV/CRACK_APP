import os
from main import app
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template,Response,send_from_directory
from werkzeug.utils import secure_filename
import cv2
import os
from camera import VideoCamera

from google_storage import Download_model_file
if not os.path.exist("static/model_final.pth"):
    print("file not present")
    Download_model_file()
else:
    print("file is present")
     
def gen(camera):
    while True:
        frame = camera.get_frame()
        frame = frame.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/', methods=['POST'])
def upload_video():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    else:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # print('upload_video filename: ' + filename)
        flash('Video successfully uploaded and displayed below')
        #return render_template('upload.html', filename=filename)
        return Response(gen(VideoCamera(filename)),mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/display/<path:filename>")
def display_video(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
    
if __name__ == '__main__':
    app.run(threaded=True)



    