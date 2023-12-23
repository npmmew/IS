from flask import Flask, render_template
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'esafauihf38i212asefaw3fhi32'

@app.route('/')
def home():
    return render_template('base.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        # Здесь обычно выполняется логика обработки данных формы
        # Например, регистрация пользователя в базе данных
        print(f'Username: {form.username.data}')
        print(f'Email: {form.email.data}')
        print(f'Password: {form.password.data}')

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        print(f'Email: {form.email.data}')
        print(f'Password: {form.password.data}')

    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)