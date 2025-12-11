# hospital_management

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
Add Patients: Register new patients with comprehensive medical information
View Patients: Browse patient lists with search and filtering capabilities
Update Patients: Edit patient details including contact information and medical history
Delete Patients: Remove patient records with confirmation
Search Patients: Advanced search by name, ID, email, or phone number
👨‍⚕️ Doctor Management
Add Doctors: Register medical professionals with specialization details
View Doctors: Browse doctor lists with department and specialization filters
Update Doctors: Modify doctor information, availability, and status
Delete Doctors: Remove doctor records with confirmation
Search Doctors: Filter by specialization, department, or name
📅 Appointment Management
Book Appointments: Schedule appointments with patient-doctor linking
View Appointments: Display appointment schedules with status tracking
Update Appointments: Modify appointment details and status
Cancel Appointments: Remove appointments with confirmation
Search Appointments: Filter appointments by date, status, or ID
🔐 Authentication & Security
Staff Registration: Secure user account creation
Staff Login/Logout: Authentication system with session management
Password Reset: Secure password recovery functionality
Role-based Access: Protected views requiring authentication
📊 Dashboard & Analytics
Staff Dashboard: Overview of key metrics and statistics
Real-time Statistics: Live counts of patients, doctors, and appointments
Today's Appointments: Quick view of daily schedules
🎨 User Interface
Responsive Design: Bootstrap-based modern UI
Mobile-Friendly: Optimized for all device sizes
Intuitive Navigation: Easy-to-use interface for healthcare staff
Admin Interface: Django admin panel for advanced management
🛠️ Technology Stack
Backend
Django 5.2.8: High-level Python web framework
Python 3.13: Programming language
MongoDB: NoSQL database for flexible data storage
PyMongo 4.15.4: MongoDB driver for Python
Frontend
HTML5: Markup language for web pages
CSS3: Styling and layout
Bootstrap 5: Responsive CSS framework
JavaScript: Client-side scripting
Development Tools
Django Bootstrap5: Bootstrap integration for Django
SQLite: Database for Django authentication (separate from MongoDB)
Git: Version control system
📋 Prerequisites
Before running this application, ensure you have the following installed:

System Requirements
Python 3.8+ (preferably Python 3.13)
MongoDB 4.0+ running on localhost:27017
Git for version control
Web browser (Chrome, Firefox, Safari, or Edge)
Python Packages
All required packages are listed in requirements.txt:

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
# Windows
python -m venv hospital_env

# Linux/Mac
python3 -m venv hospital_env
3. Activate Virtual Environment
# Windows
hospital_env\Scripts\activate

# Linux/Mac
source hospital_env/bin/activate
4. Install Dependencies
pip install -r requirements.txt
5. Apply Django Migrations
python manage.py migrate
🗄️ Database Setup
MongoDB Configuration
Start MongoDB Service

# Windows (if installed as service)
net start MongoDB

# Linux/Mac
sudo systemctl start mongod
# or
mongod
Verify MongoDB Connection

mongo
# or
mongosh
Database Structure The application automatically creates the following collections in the hospital_management database:

patients: Patient records
doctors: Doctor information
appointments: Appointment schedules
Django Authentication Database
Uses SQLite (db.sqlite3) for Django's built-in authentication system
Automatically created during migration
▶️ Running the Application
1. Start the Development Server
python manage.py runserver
2. Access the Application
Main Website: http://127.0.0.1:8000/
Admin Panel: http://127.0.0.1:8000/admin/
3. Create Superuser (Admin Access)
python manage.py createsuperuser
Follow the prompts to create an admin user for accessing the Django admin panel.

📖 Usage
For Healthcare Staff
Register/Login

Visit the homepage
Click "Staff Login" or "Staff Signup"
Create an account or login with existing credentials
Dashboard

View key statistics and today's appointments
Navigate to different sections using the menu
Patient Management

Add new patients with complete medical information
Search and filter patient records
Update patient details as needed
View patient history and appointments
Doctor Management

Register new doctors with specialization details
Update doctor availability and status
Search doctors by department or specialization
Appointment Scheduling

Book appointments linking patients with doctors
View appointment schedules
Update appointment status and details
Cancel appointments when necessary
For Administrators
Django Admin Panel
Access advanced management features
View detailed logs and system information
Manage user accounts and permissions
📁 Project Structure
hospital_management/
├── hospital/                    # Main Django project
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py             # Django settings and configuration
│   ├── urls.py                 # Main URL routing
│   └── wsgi.py
├── hospital_app/               # Main application
│   ├── __init__.py
│   ├── admin.py                # Django admin configuration
│   ├── admin_dashboard.py      # Custom admin views
│   ├── apps.py
│   ├── models.py               # Django models (for admin compatibility)
│   ├── tests.py
│   ├── urls.py                 # App URL routing
│   ├── views.py                # View functions and logic
│   ├── static/                 # Static files (CSS, JS, images)
│   │   └── images/
│   │       └── hospital-hero-bg.jpg
│   └── templates/              # HTML templates
│       ├── admin/              # Admin panel templates
│       │   └── hospital_app/
│       └── hospital_app/       # Main app templates
├── hospital_env/               # Virtual environment (created during setup)
├── db.sqlite3                  # SQLite database for authentication
├── manage.py                   # Django management script
├── requirements.txt            # Python dependencies
└── README.md                   # This file
🔗 API Endpoints
Public Endpoints
GET / - Homepage
GET /staff/signup/ - Staff registration
GET /staff/login/ - Staff login
POST /staff/logout/ - Staff logout
Protected Endpoints (Require Authentication)
GET /staff/dashboard/ - Staff dashboard
GET /patients/ - Patient list
POST /patients/add/ - Add patient
GET /patients/<id>/update/ - Update patient form
POST /patients/<id>/update/ - Update patient
POST /patients/<id>/delete/ - Delete patient
GET /doctors/ - Doctor list
POST /doctors/add/ - Add doctor
GET /doctors/<id>/update/ - Update doctor form
POST /doctors/<id>/update/ - Update doctor
POST /doctors/<id>/delete/ - Delete doctor
GET /appointments/ - Appointment list
POST /appointments/book/ - Book appointment
GET /appointments/<id>/update/ - Update appointment form
POST /appointments/<id>/update/ - Update appointment
POST /appointments/<id>/delete/ - Delete appointment
Search Endpoints
GET /search/patients/ - Search patients
GET /search/doctors/ - Search doctors
GET /search/appointments/ - Search appointments
🤝 Contributing
We welcome contributions to improve the Hospital Management System!

Development Setup
Fork the repository
Create a feature branch: git checkout -b feature-name
Make your changes
Run tests: python manage.py test
Commit changes: git commit -am 'Add feature'
Push to branch: git push origin feature-name
Submit a pull request
Code Style
Follow PEP 8 Python style guidelines
Use meaningful variable and function names
Add docstrings to functions and classes
Keep functions small and focused on single responsibilities
Testing
Write unit tests for new features
Test both positive and negative scenarios
Ensure all existing tests pass before submitting
📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🆘 Support
If you encounter any issues or have questions:

Check the Issues page on GitHub
Review this README for common setup problems
Ensure MongoDB is running and accessible
Verify all Python dependencies are installed
Check Django settings and database connections
🔄 Version History
Version 1.0.0
Initial release
Complete CRUD operations for patients, doctors, and appointments
Staff authentication system
MongoDB integration
Responsive Bootstrap UI
Django admin panel integration
🙏 Acknowledgments
Django Framework for the robust web framework
MongoDB for flexible NoSQL database capabilities
Bootstrap for responsive UI components
Python community for excellent libraries and tools
Built with ❤️ for healthcare professionals worldwide

