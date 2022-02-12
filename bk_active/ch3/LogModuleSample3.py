import logging
import logging.handlers

Log = logging.getLogger('LogModuleSample3')

LogLevel = logging.DEBUG
LogFileName = 'bk_active/ch3/LogModuleSample3.log'
LogFormat = logging.Formatter('[%(process)d|%(thread)d|%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s: %(message)s')

ConsoleHandler = logging.StreamHandler()
ConsoleHandler.setFormatter(LogFormat)

FileHandler = logging.FileHandler(LogFileName)
FileHandler.setFormatter(LogFormat)

Log.setLevel(LogLevel)
Log.addHandler(ConsoleHandler)
Log.addHandler(FileHandler)

Log.debug('DEBUG message')
Log.info('INFO message')
Log.warning('WARNING message')
Log.error('ERROR message')
Log.critical('CRITICAL message')
