from flask import Flask ,redirect ,url_for
from  flask import render_template
app = Flask(__name__)


@app.route('/')
def cv_main_page():
    return render_template('CV.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/experience')
def experience_page():
    return render_template('experience.html')

@app.route('/assignment8')
def assignment8_page():
    return render_template('assignment8.html', name='GUY ABRAMOV' , sport1='basketball' ,sport2='football' , prog='sql' , prog2='JAVA', shows=('friends' , 'superstore' , 'suits' , 'archer' , 'iron fist' , '24'))

@app.route('/header')
def header_page():
    return render_template('header.html')


if __name__ == '__main__':
    app.run(debug=True)
