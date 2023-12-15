import logging
import json

import redis

# Redis
Redis_host = None


try:
    from rest_api import settings as sets
except ModuleNotFoundError:
    import settings as sets


logger = logging.getLogger(__name__)


def connect(host=sets.REDIS_HOST, port=6379):
    global Redis_host
    logger.info(f'Connecting to redis://{host}:{port}')
    try:
        Redis_host = redis.Redis(host=host, port=port,
                                 db=sets.REDIS_DB,
                                 socket_timeout=3)

    except redis.exceptions.TimeoutError as ex:
        logger.error(ex)
        raise


def put_data(var_name, data: dict):
    logger.debug(f'Writing {data=}')
    Redis_host.set(name=var_name, value=json.dumps(data))

    if Redis_host.ping():
        logger.debug('Connection OK')


def get_data(var_name) -> dict:
    logger.debug(f'Reading {var_name=}')
    return json.loads(Redis_host.get(var_name))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    connect()
    dummy = {'timestamp': 1234, 'value': 22.4}
    put_data('realtime', dummy)
    print(get_data('realtime'))