import os



class Config(object):#inherit characteristics from Object object
    #attribute of Config
    SECRET_KEY = os.environ.get('SECRET_KEY') or "this is my secret key"
