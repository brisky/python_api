# DEFAULT VALUES
VERSION = '0.1.0'

MIN_PYTHON_VERSION = (3, 8)

DEFAULT_LOG_LEVEL = 'INFO'

LOG_FORMAT = '%(asctime)s [%(levelname)10s] %(name)10s | %(message)s'

# Simulator values

SIM_MAX_RANDOM = 100

SIM_BLINK_TIMEOUT = 2.0

# SQLite data

DATABASE_URI ='sqlite:///sensors.sqlite3'

# REST SERVER
HISTORY_URL = "http://localhost:5000/history/temperature"
REALTIME_URL = "http://localhost:5000/realtime/temperature"