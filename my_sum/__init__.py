import sys
import logging

from my_sum import settings as sets

if sys.version_info[:2] < set.MIN_PYTHON_VERSION:
    print ('Error: minimum python version; ', set.MIN_PYTHON_VERSION, 
        ' ABORTING!')
    sys.exit(1)

logging.basicConfig(filename='my_sum.log', level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('Starting my_sum version {sets.VERION}')
logger.setLevel(sets.DEFAULT_LOG_LEVEL)