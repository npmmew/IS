from flask import Flask, render_template, request
import sqlite3
import os
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(database=os.path.join(app.root_path, 'flsite.db')))
app.config['SECRET_KEY'] = 'esafauihf38i212asefaw3fhi32'


DATABASE = '/tmp/flsite.db'
DEBUG = True
SECRET_KEY = 'fgaiuhfaiuwehi2u3ohf23iouweof'


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('/user/register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route('/add_order')
def add_order():
    return render_template('/user/addorder.html')


@app.route('/history_order')
def history_order():
    return render_template('/user/history_order.html')


@app.route('/admin')
def admin():
    return render_template('/manager/mprofile.html')

if __name__ == '__main__':
    app.run(debug=True)
