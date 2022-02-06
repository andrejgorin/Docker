#!/usr/bin/env python
"""
Some helpers for python scripts
"""
import logging

FILE = "/var/log/mycron.log"


def get_logger():
    """
    Get logger object
    """
    myformat = (
        "%(asctime)s - %(levelname)s -  %(name)s"
        " - %(filename)s.%(funcName)s.%(lineno)d - %(message)s"
    )
    logger = logging.getLogger(__file__)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(FILE)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(myformat)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


mylogger = get_logger()
