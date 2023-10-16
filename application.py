from flask import Flask, render_template, request
from weather import main as get_weather

application = Flask(__name__, static_url_path='/static', static_folder='static')

@application.route('/', methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        print('post')
        city = request.form['cityName']
        state = request.form['stateName']
        country = request.form['countryName']
        if city and state and country:
            data = get_weather(city, state, country)
    return render_template('index.html', data=data)

if __name__ == '__main__':
    application.run(debug=False) # change to false when deploying
