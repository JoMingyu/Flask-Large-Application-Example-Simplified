# from sqlalchemy import create_engine


class DB(object):
    """
    DB connection helper class like standard flask 3-rd party libraries
    """
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        pass
