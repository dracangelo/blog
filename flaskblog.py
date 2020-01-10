from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '2bb074c4bb12f77596c2220f8614fd02'

posts = [
    {
        'author': 'Dan Brown',
        'title': 'Origins',
        'content': 'Best book',
        'date_posted': 'Jan 03, 2020'
    },
    {
        'author': 'terr Brown',
        'title': 'terry perry',
        'content': 'Best mag',
        'date_posted': 'Jan 23, 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = RegistrationForm()
    return render_template('login.html', title='login', form=form)



if __name__ == '__main__':
    app.run(debug=True)
