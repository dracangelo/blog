from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Dan Brown',
        'title':'Origins',
        'content':'Best book',
        'date_posted':'Jan 03, 2020'
    },
    {
        'author': 'terr Brown',
        'title':'terry perry',
        'content':'Best mag',
        'date_posted':'Jan 23, 2020'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')



if __name__=='__main__':
    app.run(debug=True)