import logging


from flask import Flask, render_template, jsonify, request
from waitress import serve
import dataset

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


@app.route('/realtime/<sensor>')
def realtime_temperature(sensor):
    db = dataset.connect(sets.DATABASE_URI)
    
    #if sensor not in db.tables:
    #    db.close()
    #    return jsonify({'error': f'Table "{sensor}" not found'})

    #table = db[sensor]
    #result = table.find_one(order_by=['-1timestamp'])
    #db.close()
    #return jsonify(result)


    #table = db['temperature']
    #result = db.query('SELECT timestamp, value FROM temperature ORDER BY timestamp DESC LIMIT 1')
    #data = [row for row in result]    

#@app.route('/history/<sensor>')
#def history(sensor):
    #db = dataset.connect(sets,DATABASE_URI)
    #if sensor not in db.tables:
    #    db.close()
    #    return jsonify({'error': f'Table "{sensor}" not found'})

    #table = db[sensor]
    #result = table.find_one(order_by['-timestamp'])
    #db.close()
    #return jsonify(data)

    #db = dataset.connect(sets.DATABASE_URI)
    #table = db['temperature']
    #result = table.find(order_by=['-1timestamp'], _limit=max)
    #data = [row for row in result]
    
@app.route('/history/<sensor>')
def history_temperature(sensor):
    try:
        max = int(request.args.get('max', default=100))
        logger.debug(f'{max=}')
    except:
        max = 100

    db = dataset.connect(sets.DATABASE_URI)
    table = db[sensor]
    result = table.find(order_by=['-timestamp'], _limit=max)
    data = [row for row in result]
    db.close()
    return jsonify(data)  

    #result = db.query('SELECT timestamp, value FROM temperature ORDER BY timestamp DESC LIMIT {max}')
    #data = [row for row in result]
    #return jsonify(data[-1])
    #table = db['temperature']
    #data = []



def main():
    serve(app, listen='*:5000')


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000, debug=True)
    serve(app, listen='*:5000')
