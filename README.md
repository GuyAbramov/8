
console.log('inside fetch example');


function getUsers(){
    console.log('clicked');
    fetch('https://reqres.in/api/users').then(
        response => response.json()
    ).then(
        response_obj => put_users_inside_html(response_obj.data)
    ).catch(
        err => console.log(err)
    )
}

function put_users_inside_html(response_obj_data) {
    // console.log(response_obj_data);

    const curr_main = document.querySelector("main");
    for (let user of response_obj_data) {
        const section = document.createElement('section');
        section.innerHTML = `
        <img src="${user.avatar}" alt="Profile Picture"/>
        <div>
            <span>${user.first_name} ${user.last_name}</span>
            <br>
            <a href="mailto:${user.email}">Send Email</a>
        </div>
        `;
        curr_main.appendChild(section);
    }
}






console.log('inside fetch example');


function getUsers(){
    console.log('clicked');
    fetch('https://reqres.in/api/users').then(
        response => response.json()
    ).then(
        response_obj => put_users_inside_html(response_obj.data)
    ).catch(
        err => console.log(err)
    )
}

function put_users_inside_html(response_obj_data) {
    // console.log(response_obj_data);

    const curr_main = document.querySelector("main");
    for (let user of response_obj_data) {
        const section = document.createElement('section');
        section.innerHTML = `
        <img src="${user.avatar}" alt="Profile Picture"/>
        <div>
            <span>${user.first_name} ${user.last_name}</span>
            <br>
            <a href="mailto:${user.email}">Send Email</a>
        </div>
        `;
        curr_main.appendChild(section);
    }
}

app.py
@app.route('/assignment11/outer_source')
def assignment11_def():
    if 'user_num' in request.form:
        user_num = request.form['user_num']
        return render_template('assignment11.html', user_num=user_num)
    return render_template('assignment11.html')


ass11

{% extends 'base.html' %}
{% block title%}
 ass11
{% endblock %}

{% block body %}
    <script src="../static/js/fetch.js"></script>
<h3>User Number:<input type="number" name="user_num" placeholder="1-12"> <br></h3>

    <button  onclick="getUsers()">Get User</button>
    <div id="output"></div>

    <hr>
    <h3>here</h3>
    {{ user_num }}
    <hr>
<main>


</main>

    {% endblock %}
