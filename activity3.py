from flask import Flask, render_template
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    return render_template('user.html', name = "Sean", current_time=datetime.utcnow())

