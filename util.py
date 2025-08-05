
import logging

class CustomFormatter(logging.Formatter):

    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format1 = bold_red + "%(asctime)s - %(name)s - %(levelname)s -" + reset
    format2 = ' %(message)s ' 
    format3 = bold_red +  "(%(filename)s:%(lineno)d)" + reset

    FORMATS = {
        logging.DEBUG: format1 + grey + format2 + reset + format3,
        logging.INFO: format1 + grey + format2 + reset + format3,
        logging.WARNING: format1 + yellow + format2 + reset + format3,
        logging.ERROR: format1 + red + format2 + reset + format3,
        logging.CRITICAL: format1 + bold_red + format2 + reset + format3
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

# create logger
def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(CustomFormatter())
    logger.addHandler(ch)
    return logger

