#!/usr/bin/python3
from . import settings
from datetime import datetime

class Logger(object):
	def __init__(self):
		pass

	def log_event(self, _text, event_type=0):
		logfile = open(settings.LOG_PATH,'a')
		logfile.write(settings.LOG_FORMAT.format(curdate=datetime.now(), event_type=event_type, data=_text))
		logfile.close()

	def log_error(self, _text):
		logfile = open(settings.ERROR_LOG_PATH, 'a')
		logfile.write(settings.LOG_FORMAT.format(curdate=datetime.now(), event_type='ERROR', data=_text))
		logfile.close()
