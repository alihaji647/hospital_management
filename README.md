# hospital_management
🏥 Hospital Management System

A comprehensive web-based hospital management system built with Django and MongoDB, designed to streamline patient management, doctor scheduling, and appointment booking for healthcare facilities.

📋 Table of Contents

Features

Technology Stack

Prerequisites

Installation

Database Setup

Running the Application

Usage

Project Structure

API Endpoints

Contributing

License

✨ Features
👥 Patient Management

Register new patients with complete medical information

View, update, delete patient records

Advanced search by name, ID, email, phone

👨‍⚕️ Doctor Management

Add and manage doctor profiles

Filter by specialization or department

Update availability and status

📅 Appointment Management

Book, update, cancel appointments

Track appointment status

Search by date, ID, status

🔐 Authentication & Security

Staff registration & login

Password reset

Role-based protected views

📊 Dashboard & Analytics

Staff dashboard with real-time statistics

Today’s appointment overview

🎨 User Interface

Fully responsive (Bootstrap 5)

Mobile friendly

Clean navigation

Django admin support

🛠️ Technology Stack
Backend

Django 5.2.8

Python 3.13

MongoDB (NoSQL)

PyMongo 4.15.4

Frontend

HTML5, CSS3

Bootstrap 5

JavaScript

Tools

Django Bootstrap5

SQLite (for authentication)

Git

📋 Prerequisites
System

Python 3.8+ (recommended: 3.13)

MongoDB 4.0+

Git

Web browser

Python Packages (from requirements.txt)
asgiref==3.11.0
Django==5.2.8
django-bootstrap5==25.3
dnspython==2.8.0
pymongo==4.15.4
sqlparse==0.5.3
tzdata==2025.2

🚀 Installation
1. Clone the Repository
git clone https://github.com/usamasaeed911/hospital_management
cd hospital_management

2. Create Virtual Environment
python -m venv hospital_env

3. Activate Virtual Environment

Windows

hospital_env\Scripts\activate


Linux/Mac

source hospital_env/bin/activate

4. Install Dependencies
pip install -r requirements.txt

5. Apply Migrations
python manage.py migrate

🗄️ Database Setup
Start MongoDB

Windows

net start MongoDB


Linux/Mac

sudo systemctl start mongod

Verify Connection
mongosh

MongoDB Collections (auto-created)

patients

doctors

appointments

Django Authentication

Uses SQLite (db.sqlite3)

Auto-created on migration

▶️ Running the Application
1. Start Server
python manage.py runserver

2. Access

Main App → http://127.0.0.1:8000/

Admin Panel → http://127.0.0.1:8000/admin/

3. Create Admin User
python manage.py createsuperuser

📖 Usage
Staff Workflow

Sign up or login

Access dashboard

Manage patients, doctors, appointments

Administrator Features

Manage users

View logs

Advanced admin tools via Django admin

📁 Project Structure
hospital_management/
├── hospital/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── hospital_app/
│   ├── admin.py
│   ├── admin_dashboard.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── static/
│   └── templates/
├── db.sqlite3
├── requirements.txt
├── manage.py
└── README.md

🔗 API Endpoints
Public
Method	Endpoint	Description
GET	/	Homepage
GET	/staff/signup/	Staff Sign Up
GET	/staff/login/	Staff Login
POST	/staff/logout/	Logout
Protected (Login Required)

Patients, Doctors, Appointments CRUD endpoints exactly as provided.

🤝 Contributing
Steps

Fork repository

Create branch

Commit changes

Push

Create pull request

Guidelines

Follow PEP8

Write unit tests

Use meaningful names

📄 License

Licensed under the MIT License.

🆘 Support

Check GitHub Issues

Confirm MongoDB is running

Verify package installation

Check Django settings

🔄 Version History
v1.0.0

Initial release with complete CRUD

Staff auth

MongoDB integration

Responsive UI

🙏 Acknowledgments

Django

MongoDB

Bootstrap

Python community
