import logging


class Master:
    def __init__(self):
        app_name = self.__class__.__name__
        logging.basicConfig()
        self.logger = logging.getLogger(app_name)
        self.logger.setLevel(logging.INFO)


