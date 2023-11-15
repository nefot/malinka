import logging
import os


def setup_logging():
    log_directory = 'log'
    os.makedirs(log_directory, exist_ok=True)
    log_filename = 'app.log'
    log_path = os.path.join(log_directory, log_filename)
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler(log_path, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.propagate = False
    return logger

logger = setup_logging()