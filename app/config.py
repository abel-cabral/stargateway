import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SERVICE_1_URL = os.environ.get('SERVICE_1_URL')
    SERVICE_2_URL = os.environ.get('SERVICE_2_URL')