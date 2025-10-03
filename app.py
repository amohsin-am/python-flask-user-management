from flask import Flask, redirect, url_for, request, render_template
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

cnx = mysql.connector.connect(
    host=os.getenv("DB_HOST", "localhost"),
    port=int(os.getenv("DB_PORT", "3306")),
    user=os.getenv("DB_USER", "root"),
    password=os.getenv("DB_PASS", ""),
    database=os.getenv("DB_NAME", "batch_6")
)
cursor = cnx.cursor()

@app.route('/')
def hello():
    return render_template(
        'home.html',
        page_type="Home",
        my_num=0,
        my_list=["Apple", "Orange", "Mango", "Cherry", "Banana"]
    )

@app.route('/admin/', methods=['POST', 'GET'])
def admin_1():
    if request.method == "POST":
        users_name  = request.form['user_name']
        users_email = request.form['email']
        users_city  = request.form['user_city']
        users_hobby = request.form['user_hobby']

        cursor.execute(
            "INSERT INTO users (user_name, email, city, hobby) VALUES (%s, %s, %s, %s)",
            (users_name, users_email, users_city, users_hobby)
        )
        cnx.commit()
        return redirect(url_for('user_data')) 

    return render_template('home.html', page_type="Admin", my_num=1, my_list=["Alpha","Beta"])


@app.route('/user_name/<user_name>')
def user(user_name):
    return render_template('home.html', page_type=user_name, my_num=2, my_list=["One","Two"])

@app.route('/type/<user_type>')
def user_type(user_type):
    if user_type == "admin":
        return redirect(url_for('admin_1'))
    else:
        return redirect(url_for('user', user_name=user_type))

@app.route('/user_form/')
def user_form():
    return render_template('test.html')

@app.route('/user_data/')
def user_data():
    cursor.execute("SELECT id, user_name, email, city, hobby FROM users;")
    users_list = cursor.fetchall()
    return render_template('user_data.html', user_data_list=users_list)

@app.route('/profile/<user_id>/')
def user_profile(user_id):
    cursor.execute("SELECT id, user_name, email, city, hobby FROM users WHERE id = %s", (user_id,))
    users_profile = cursor.fetchone()
    return render_template('profile.html', user_profile=users_profile)

@app.route('/delete_user/<user_id>/')
def delete_profile(user_id):
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    cnx.commit()
    return redirect(url_for('user_data'))


@app.route('/add', methods=['GET', 'POST'])
def add_spec():
    if request.method == 'GET':
        return render_template('test.html')

    users_name  = request.form['user_name']
    users_email = request.form['email']
    users_city  = request.form['user_city']
    users_hobby = request.form['user_hobby']

    cursor.execute(
        "INSERT INTO users (user_name, email, city, hobby) VALUES (%s, %s, %s, %s)",
        (users_name, users_email, users_city, users_hobby)
    )
    cnx.commit()
    return redirect(url_for('users_spec'))

@app.route('/users')
def users_spec():
    cursor.execute("SELECT id, user_name, email, city, hobby FROM users;")
    users_list = cursor.fetchall()
    return render_template('user_data.html', user_data_list=users_list)

@app.route('/user/<int:user_id>')
def user_spec(user_id):
    cursor.execute("SELECT id, user_name, email, city, hobby FROM users WHERE id=%s", (user_id,))
    users_profile = cursor.fetchone()
    return render_template('profile.html', user_profile=users_profile)

@app.route('/delete/<int:user_id>', methods=['POST', 'GET'])
def delete_spec(user_id):
    cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
    cnx.commit()
    return redirect(url_for('users_spec'))

if __name__ == '__main__':
    app.run(port=5000, debug=True)
