import cv2
import numpy as np
import torch, torchvision
import detectron2
from detectron2 import model_zoo
from detectron2.utils.logger import setup_logger
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog, DatasetCatalog

from detectron2.engine import DefaultTrainer
from detectron2.data.datasets import register_coco_instances

class VideoCamera(object):
    def __init__(self,filename):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.filename = filename
        #self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        self.video = cv2.VideoCapture(f'static/uploads/{self.filename}')
        
        print("came into init classs")
        register_coco_instances("customtrain1", {}, "./instances_train.json", "./train")
        sample_metadata = MetadataCatalog.get("customtrain1")
        dataset_dicts = DatasetCatalog.get("customtrain1")
        cfg = get_cfg()
        cfg.merge_from_file(model_zoo.get_config_file("COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml"))
        cfg.DATASETS.TRAIN = ("customtrain1",)
        cfg.DATALOADER.NUM_WORKERS = 2
        cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml")  # Let training initialize from model zoo
        cfg.SOLVER.IMS_PER_BATCH = 2
        cfg.SOLVER.BASE_LR = 0.0025  # pick a good LR
        cfg.SOLVER.MAX_ITER = 700    # 300 iterations seems good enough for this toy dataset; you will need to train longer for a practical dataset
        cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = 128   # faster, and good enough for this toy dataset (default: 512)
        cfg.MODEL.ROI_HEADS.NUM_CLASSES = 6  # (see https://detectron2.readthedocs.io/tutorials/datasets.html#update-the-config-for-new-datasets)
        cfg.MODEL.WEIGHTS = "static/uploads/model_final.pth"
        cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5   # set the testing threshold for this model
        cfg.DATASETS.TEST = ()
        self.predictor = DefaultPredictor(cfg)
        print("compleated loading the predictor")
        


    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        '''
        outputs = self.predictor(image)
        v = Visualizer(image[:, :, ::-1],
                       metadata=sample_metadata, 
                       scale=0.8, 
                       instance_mode=ColorMode.IMAGE_BW)   # remove the colors of unsegmented pixels)
        v = v.draw_instance_predictions(outputs["instances"].to("cpu"))
        image = v.get_image()[:, :, ::-1]
        '''
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg


