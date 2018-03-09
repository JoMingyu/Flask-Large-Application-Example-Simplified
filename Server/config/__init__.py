import os


class Config(object):
    REPRESENTATIVE_HOST = None
    PORT = 3000

    SECRET_KEY = os.getenv('SECRET_KEY', '85c145a16bd6f6e1f3e104ca78c6a102')
    # Secret key for any 3-rd party libraries
