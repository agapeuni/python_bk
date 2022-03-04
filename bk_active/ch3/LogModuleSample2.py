import logging

LogFormatter = '[%(process)d|%(thread)d|%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s: %(message)s'
logging.basicConfig(level=logging.INFO,
                    filename='bk_active/ch3/LogModuleSample2.log', format=LogFormatter)

logging.debug('DEBUG message')
logging.info('INFO message')
logging.warning('WARNING message')
logging.error('ERROR message')
logging.critical('CRITICAL message')
