import argparse
import logging

logger = logging.getLogger(__name__)

try:
    from my_sum import functions as fn
    from my_sum import settings as sets
except ModuleNotFoundError:
    import functions as fn
    import settings as sets


if __name__ == '__main__':
    # print(fn.my_int_sum(10, 10))
    parser = argparse.ArgumentParser(
        prog = 'my_sum',
        description="It sums two int numbers"
    )
    parser.add_argument('a', type=int)
    parser.add_argument('b', type=int)
    parser.add_argument('--version', action='version', version=(f'v{sets.VERSION}'))
    parser.add_argument('--verbose', '-v', action='count', default=0)
    args = parser.parse_args()

    if args.verbose == 1:
        logger.setLevel('INFO')
    elif args.verbose >= 2:
        logger.setLevel('DEBUG')

    print( fn.my_int_sum(args.a, args.b))