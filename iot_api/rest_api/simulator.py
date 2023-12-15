import logging
import random
import datetime as dt, time
from random import random

try:
    from rest_api import settings as sets
except ModuleNotFoundError:
    import settings as sets

logger = logging.getLogger(__name__)

Counter = 0 
Blink = True
Last_blink_time = dt.datetime.now()

def random_number(max_value=100, digits=2):
    return round(random() * max_value, digits)

def get_and_inc_counter():
    global Counter 
    Counter += 1
    return Counter

def get_blink():
    now = dt.datetime.now()
    global Blink
    global Last_blink_time
    if (now - Last_blink_time).total_seconds() > sets.SIM_BLINK_TIMEOUT:
        Last_blink_time = now
        Blink = not Blink
    
    return Blink

if __name__ == '__main__':
    # print(rando_number())
    x = random_number()
    assert x < sets.SIM_MAX_RANDOM
    x = random_number(10)
    assert x < 10

    assert Counter == 0
    get_and_inc_counter()
    assert Counter > 0 

    assert Blink
    time.sleep(sets.SIM_BLINK_TIMEOUT)
    get_blink()
    assert not Blink

