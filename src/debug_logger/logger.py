import os
import threading

from inspect import Traceback
from datetime import datetime

TAG_DEBUG = 'D'
TAG_INFO = 'I'
TAG_WARNING = 'W'
TAG_ERR = 'E'


def log(message: str, frame: Traceback, tag: str = TAG_DEBUG, class_name: str = None):
    file_name = os.path.basename(frame.filename)
    if class_name is None:
        print('{} [{}:{}] [{}][{}] {} - ({}, line:{})'.format(
            datetime.now(), os.getpid(), threading.get_ident(), tag, frame.function, message, file_name, frame.lineno))
    else:
        print('{} [{}:{}] [{}][{}][{}] {} - ({}, line:{})'.format(
            datetime.now(), os.getpid(), threading.get_ident(),
            tag, class_name, frame.function, message, file_name, frame.lineno))
