### Flask User Management System

## 📌 Overview

A simple Flask web application that allows users to:

Add new users via a form

View all users in a list

View each user's detailed profile

Delete users

This project demonstrates integration between Flask (Python backend), MySQL database, and Bootstrap frontend.

## 🛠 Tech Stack

Backend: Python (Flask)

Database: MySQL

Frontend: HTML, CSS, Bootstrap

Version Control: Git & GitHub

## 🗄 Database Design

Table: users

Column Name	Data Type	Description
id	INT, PK, Auto Increment	Unique user ID
user_name	VARCHAR(50)	Full Name
email	VARCHAR(100)	Email Address
city	VARCHAR(50)	City Name
hobby	VARCHAR(50)	Hobby
## 📂 Project Structure
Python_final_project/
│── app.py                # Main Flask app
│── .env                  # Environment variables (DB credentials)
│── .gitignore            # Git ignore rules
│── templates/            # HTML templates
│    ├── base.html
│    ├── home.html
│    ├── add_user.html
│    ├── users.html
│    ├── profile.html
│── static/               # Static files (CSS/JS)
│    └── style.css

## ▶️ Running the Project
1. Clone the repository
git clone https://github.com/amohsin-am/python-flask-user-management.git
cd python-flask-user-management

2. Create a virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate   # On Mac/Linux

3. Install dependencies
pip install flask mysql-connector-python python-dotenv

4. Set up MySQL database

 - Run the following SQL commands in MySQL Workbench:
 - CREATE DATABASE IF NOT EXISTS batch_6;
 - USE batch_6;
 - CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    city VARCHAR(50) NOT NULL,
    hobby VARCHAR(50) NOT NULL
);

5. Configure environment variables

  - Create a .env file in the root project folder:

    - DB_HOST=localhost
    - DB_PORT=3306
    - DB_USER=root
    - DB_PASS=your_password
    - DB_NAME=batch_6

6. Run the Flask app
  - python app.py
      - Visit: http://127.0.0.1:5000/

## 🚀 Features

✅ Add User (via form)

✅ View All Users (list)

✅ View Profile (detailed page)

✅ Delete User

## 🤝 Contribution

  - Abhay
  - GitHub
  - Google
  - ChatGPT
  - Gemini


## 📜 License

This project is open-source and available under the MIT License.
