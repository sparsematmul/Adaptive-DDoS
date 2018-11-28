
import logging




def loggingSetup():
	statsLogger = logging.getLogger('statsLogger')

	debugLogger = logging.getLogger('debugLogger')

	debugLogger.setLevel(logging.DEBUG)
	statsLogger.setLevel(logging.INFO)
	# create file handler which logs even debug messages
	fh = logging.FileHandler('debug.log')
	fh.setLevel(logging.DEBUG)
	# create console handler with a higher log level
	ch = logging.FileHandler('stats.log')
	ch.setLevel(logging.INFO)
	# create formatter and add it to the handlers
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	ch.setFormatter(formatter)
	fh.setFormatter(formatter)
	# add the handlers to logger
	statsLogger.addHandler(ch)
	debugLogger.addHandler(fh)

