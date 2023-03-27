from google.cloud import storage
from google.cloud import storage as dns
from google.oauth2 import service_account

def Download_model_file():  
  gcp_sa_credentials = {
    "type": "service_account",
    "project_id": "essential-oasis-351023",
    "private_key_id": "36fee209b1708ce76d0846559a65d0ea2984a25d",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCJtAU2pxGooQLc\nGEhThG3mbIeEiow5rG+pezjW92lDgSyYFslCgzYyetQB8yjLzRhMV/ACsk1BAzCa\nIAJrlTb3Vf/ablGjipcTAcKbBy9rBCef/2PYxK8qLXNuIcpSktPX4zZEFCNAvYil\nBumA4LjmfRcWLUqTKdRIAwfMrTHmrvDZ8xl1MZIZPQ/TpTGTOzVAqtXsGWWgBzyg\n7IOJmEL0EXwh14dKOFUH91nLpyyQ9DhTk2wIxvdv2JSxLlojGXWqNudpW37IYM1F\nVaShidYXjClULjTz15IxNnCBXZKXMO8c01o0KZbXb6iBfdS+Nzzad9jQoUD2zOEM\nYEITCe55AgMBAAECggEAAs3uz2pXN1oBx5x60vDxoYrwjBwbvLwfVozpmeQrnu9e\nqoFyoMcwvNYITbqyEst8TRK7PZImyrYJ9iZEfQSAEZ5iYcRpJyWLi9yCG3uUb+94\n2fRJiD4Xi1T7YrZEtfTi+a9j46lNf1QqLXfkHHGHMSeB8hFNprddfnLJr1W60aXo\nX5QB10V2PezUFG1kH1tmsNsrvsKNKn4fGPQMZzOv4dejngAIxYLn7mkReCXDSwBs\n7nAtNYVP17DpoqHPauENgWYCpqmR7CJRKxLsnHA56L7k4TmvOZP5VQJ0YndmvYkP\n9HsqbKdTQcBKSzAzhlzzUGjHVe3s0EQvwmyOBW7oMQKBgQDB7frjSrJenbeNm84d\n9KD2SxJRrZSR9RCnV+naXmoyepqQ4jxU+u4SabdOxFdPDKCeFYWTnrgKBtOr0lUK\nmiQaJKm4VxBlw8Qz55RgqzUyh3TI8tH9qE4JJc2IjfqNKmDYSrryTh4eBTXnuFeN\nKIPr1F70MIhd7L1oeHcawdOCUQKBgQC1xwO+RKbaijiKAk0Kmu4FuJLARoy0daSc\nQXI4qR7pbdkxgFOP7rMZYD4BF+gCASXcztP7E5+YsGSAGyALUiwx8y3tuMBSEGK2\ndg5dz1iXlKLrpVFbU9euFN977N/mlLzQmtExhHMUC+Sh2pCFaaN9pQ0vpOHZVy5O\nZmjK3vG3qQKBgENN7anercMKp76c2U8qLIbuDQCN5qc1Tz9U0pN3+xFj3ar06Y1w\nvRlk2TqcB9Umg8P5oi9WgXbxYZsbV2pjjq4IFWMlzEoVRE3jTGq0YLUVr+Fh7KFF\nPTgNh6Sh6df+YjgOz4zysZ8nncq6/p+99PLu9Ll48oruc9oDHQsLQ/XRAoGARDAL\nb2xBSulenCaQz9GeR/cc1ZOhZHBc92B1gFuwhM/4EWGZ9vwLoxE/MRnOpjHYCiRr\n0FtkGtrQWF3Uf2qruXEHYY1UV3ReEyPl77q/+NyA4PR6uE+TMHIUA2Cv/Mb+rSHm\nJzUQFg0ADtb2L5WZBqDLeXvYXLcfX7l6xd8rvUECgYAqFCMqJYg+b4MTnSDY9rWY\nlTy0aFQ1Ko38pIc+qZtgAgmh3Zd9AX54RSVt7PXyfpuRJ+jIWAXY+TPyzA018JZX\nvzECQ8yyCbIZ6vZ8SMINxyjUBNuz4XhzTz68llYKHOhJCNP2N0S21COO0Q6JSJjZ\nMbYgNeDXVzmBry0cYRzW2Q==\n-----END PRIVATE KEY-----\n",
    "client_email": "gautam@essential-oasis-351023.iam.gserviceaccount.com",
    "client_id": "101503556387915816954",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/gautam%40essential-oasis-351023.iam.gserviceaccount.com"
  }
  project_id=gcp_sa_credentials["project_id"]
  credentials = service_account.Credentials.from_service_account_info(gcp_sa_credentials)
  client = dns.Client(project=project_id,credentials=credentials)
  bucket  = client.get_bucket('detectronbucket')
  blob = bucket.blob("model_final.pth")
  blob.download_to_filename("static/model_final.pth")


