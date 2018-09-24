from pathlib import Path
import logging


def log():
    log_path = Path('log.text')
    FORMAT = '%(asctime)s %(thread)d %(threadName)s %(funcName)s %(levelno)s %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.INFO, filename=log_path)
    console = logging.StreamHandler()  # 输出至控制台
    console.setLevel(logging.INFO)
    formatter = logging.Formatter(FORMAT)
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    return logging


