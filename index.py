from flask import Flask
import fastf1 as ff1

# ff1.Cache.enable_cache('cache')


app = Flask(__name__)


@app.route('/')
def home():
    session = ff1.get_session(2023, 'Bahrain Grand Prix', 'Q')
    session.load()
    ver_lap = session.laps.pick_driver('VER').pick_fastest()
    print(ver_lap['Time'])
    return str(ver_lap['Time'])


@app.route('/about')
def about():
    return 'About'


if __name__ == '__main__':
    app.run(debug=True)
