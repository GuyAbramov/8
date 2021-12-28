from flask import Flask, redirect, url_for, request
from flask import render_template, session
from interact_with_DB import interact_db
app = Flask(__name__)
app.secret_key = '123'

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

users = {
    'GUY': {'name': 'guy', 'email': 'g12@gmail.com'},
    'GAYA': {'name': 'gaya', 'email': 'g1234@gmail.com'},
    'GALIT': {'name': 'galit', 'email': 'g234@gmail.com'},
    'GITI': {'name': 'giti', 'email': 'g65@gmail.com'},
    'GOYA': {'name': 'goya', 'email': 'g1@gmail.com'}
}

@app.route('/assignment9', methods=['GET','POST'])
def search_9():


    if request.method == 'GET':
        if 'name' in request.args and 'email' in request.args and 'is_submit' in request.args:
            name = request.args['name']
            email = request.args['email']
            is_submit = request.args['is_submit']


            for value in users.values():
                if(value.get("name") == name and value.get("email") == email):
                    return render_template('assignment9.html', name=name, email=email)


            if(is_submit):
                return render_template('assignment9.html', users=users)
        return render_template('assignment9.html')


    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        if 'username' in request.form:
            session['username'] = username
            return render_template('assignment9.html', username=username)


@app.route('/logout')
def logout_func():
    session['username'] = ''
    return render_template('assignment9.html')


if __name__ == '__main__':
    app.run(debug=True)








# @app.route('/users')
# def users_page():
# query = 'select * from users':
# users = interact_with_DB(query=query, query_type='fetch')

# return render_template('users.html', users='users')