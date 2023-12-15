""" Business login for my_sum """
import doctest
import logging

logger = logging.getLogger(__name__)

#%% function
def my_int_sum(a: int, b=0):
    """ Sum's two int numbers
    >>> my_int_sum(2, 2)
    4
    >>> my_int_sum(2, 0)
    2
    >>> my_int_sum(a=4, b=4)
    8
    """
    result = a + b
    logger.debug(f'{result=}')
    return result

#%% main

print(__name__)
if __name__ == '__main__':
    #Exploratory tests
    print(my_int_sum(2, 2))
    print(my_int_sum(2, 0))
    print(my_int_sum(a=4, b=4))

    doctest.testmod()
