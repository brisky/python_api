import logging

from flask import Flask, render_template, jsonify, request
from waitress import serve

logger = logging.getLogger(__name__)

try:
    from rest_api import settings as sets
    from rest_api import simulator as sim
except ModuleNotFoundError:
     import settings as sets
     import simulator as sim

app = Flask(__name__)

@app.route('/')
def index():
    #return "Hello World!"
    logger.info('Get Index page')
    return render_template('index.html', version=sets.VERSION)

@app.route('/simulator')
def simulator():

    try:
        max_random = int(request.args.get('max_random', default=100))
        logger.debug(f'{max_random=}')
    except ValueError:
        max_random = 100
    
    return jsonify({'random': sim.random_number(max_random),
                    'counter': sim.get_and_inc_counter(),
                    'blink': sim.get_blink()})

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000, debug=True)
    serve(app, listen='*:5000')
