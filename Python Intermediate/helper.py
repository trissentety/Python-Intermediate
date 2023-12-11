import logging
logger = logging.getLogger(__name__) #create logger in module

#create handler. log handlers responsible for dispatching appropriate log message to handlers specific destination
#Exanple use difference log handlers to send log messages to this standard output stream to files via HTTP or via email
stream_h = logging.StreamHandler() #logs to stream stream handler, built in StreamHandler class
file_h = logging.FileHandler('file.log') #file handler that logs to file, requires name

#Typially for each handler, set level and format
#level and format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR) #file handler should only log messages of logging.ERROR

#specify formatters
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s') #provide string simiilar to basic config
#set fomatter to handler
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

#Add handler to logger
logger.addHandler(str)
logger.addHandler(file_h)

#use logger to log something
logger.warning('this is a warning') #__main__ = WARNING - this is a warning
logger.error('this is an error') #__main__ ERROR - this is an error

#file.log txt file created contains __main__ - ERROR - this is an error
