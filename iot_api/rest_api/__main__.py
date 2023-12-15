
import logging
import threading

try:
    from rest_api import webserver
    from rest_api import mqtt_client
    from rest_api import dashboard
except ModuleNotFoundError:
    import webserver
    import mqtt_client
    import dashboard

if __name__ == '__main__':
    logging.info('Starting webserver module')
    threading.Thread(target=webserver.main).start()
    logging.info('Starting mqtt_client module')
    threading.Thread(target=mqtt_client.main).start()
    logging.info('Starting dashboard module')
    threading.Thread(target=dashboard.main).start()