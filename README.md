# Student Housing Platform 

Web platform developed with **Django** for managing student housing .

The application allows students to search for student houses, view available rooms, and send booking requests.  
Administrators can manage cities, houses, rooms, and reservation requests.

---

##  Technologies
- Python
- Django
- SQLite
- HTML / CSS
- Git & GitHub

---

##  Project Objectives
- Develop a professional web application using Django
- Apply MVT (Model–View–Template) architecture
- Manage a relational database
- Implement room availability and booking logic
- Work collaboratively using GitHub

---

##  User Roles

### Visitor
- View cities
- View student houses
- View available rooms

### Student
- Create an account
- Log in / log out
- Send booking requests
- View booking status

### Administrator
- Manage cities
- Manage student houses
- Manage rooms
- Accept or reject booking requests

---

##  Installation & Setup

### 1. Clone the repository
git clone https://github.com/tijabdel/Digital-Creativity.git

cd Digital-Creativity


### 2. Create virtual environment
python -m venv .venv
.venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Apply migrations
python manage.py migrate

### 5. Create admin account
python manage.py createsuperuser


### 6. Run the server
python manage.py runserver


Open in browser:


http://127.0.0.1:8000/


Admin panel:


http://127.0.0.1:8000/admin/


---

##  Project Structure



Digital-Creativity/
│
├── config/ # Django settings
├── housing/ # Main backend application
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── admin.py
│
├── templates/ # HTML templates
├── manage.py
├── requirements.txt
└── README.md
