import logging.handlers

class GetLogger():
    logger = None
    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            cls.logger = logging.getLogger()
            cls.logger.setLevel(logging.INFO)
            StreamHandler = logging.StreamHandler()
            TimedFileHandler = logging.handlers.TimedRotatingFileHandler(filename="../logs/log.log",
                                                                         when="midnight",
                                                                         interval=1,
                                                                         backupCount=30,
                                                                         encoding="utf-8")
            fmt = '%(asctime)s %(levelname)s [%(name)s] | %(filename)s(%(funcName)s:%(lineno)d) | - %(message)s'
            fm = logging.Formatter(fmt)
            StreamHandler.setFormatter(fm)
            TimedFileHandler.setFormatter(fm)
            cls.logger.addHandler(StreamHandler)
            cls.logger.addHandler(TimedFileHandler)
        return cls.logger

if __name__ == '__main__':
    logger = GetLogger.get_logger()
    logger.info("sssss")