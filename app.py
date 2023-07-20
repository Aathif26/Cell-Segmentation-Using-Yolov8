from cellSegmentation.logger import logging
from cellSegmentation.exception import AppEception
import sys

logging.info("Welcome to the custom log")

try:
    a = 4/"6"


except Exception as e:
    raise AppEception(e, sys)