import logging

logger = logging.getLogger(__name__)  # get root logger
logger.setLevel(logging.DEBUG)


def log(info_text, *args, type="info", ):
    try:
        if type == "info":
            logger.info(info_text.format(*args))
        elif type == "debug":
            logger.debug(info_text.format(*args))
    except Exception as e:
        print(e)
        pass