import logging
import time
from logging.handlers import TimedRotatingFileHandler #creates a rotating lock based on how much time is passed
 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# s, m, h, d, midnight, w0 (monday), w1 (tuesday)
# This will create a new log file every minute, and 5 backup files with a timestamp before overwriting old logs.
handler = TimedRotatingFileHandler('timed_test.log', when='s', interval=5, backupCount=5) #when rotate every, at interval 5, backup of 5 files
logger.addHandler(handler)
 
for i in range(6):
    logger.info('Hello, world!')
    time.sleep(5) #import time sleep seconds

#creates new files named timed_test.log.2023-12-05_07-53-36

