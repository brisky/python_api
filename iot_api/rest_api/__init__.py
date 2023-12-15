import sys
import logging

from rest_api import settings as sets

if sys.version_info[:2] < sets.MIN_PYTHON_VERSION:
    print ('Error: minimum python version; ', sets.MIN_PYTHON_VERSION,
        ' ABORTING!')
    sys.exit(1)

logging.basicConfig(level=logging.INFO, format=sets.LOG_FORMAT)
logger = logging.getLogger(__name__)
logger.info(f'Starting my_sum version {sets.VERSION}')
logger.setLevel(sets.DEFAULT_LOG_LEVEL)