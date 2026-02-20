# Auth App

A secure authentication and registration system built with Flask and SQLAlchemy.

## Features

- **User Registration** with comprehensive server-side validation
  - Name validation (not empty)
  - Email validation (not empty and unique)
  - Password validation (minimum 6 characters)
  - Prevents duplicate email registration
  
- **User Login** with secure authentication
- **Modern Frontend Design** with Bootstrap 5
  - Responsive gradient-based UI
  - Professional form layouts
  - Flash message alerts for user feedback

## Tech Stack

- **Backend**: Flask with SQLAlchemy ORM
- **Database**: SQLite
- **Frontend**: Bootstrap 5, HTML, CSS
- **Python Version**: 3.x

## Project Structure

```
Authapp/
├── app.py                 # Main Flask application
├── templates/             # HTML templates
│   ├── base.html         # Base template with navbar
│   ├── index.html        # Home page
│   ├── register.html     # Registration page
│   └── login.html        # Login page
├── static/               # Static files (CSS, JS, images)
├── instance/             # SQLite database file
└── README.md            # This file
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Kushagra-SethG/Authapp.git
cd Authapp
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install flask flask-sqlalchemy
```

## Running the Application

1. Navigate to the project directory
2. Activate the virtual environment
3. Run the Flask app:
```bash
python app.py
```

4. Open your browser and go to `http://127.0.0.1:5000`

## API Routes

- `GET /` - Home page
- `POST /` - Submit employee form
- `GET /register` - Registration page
- `POST /register` - Register new user with validation
- `GET /login` - Login page
- `POST /login` - User login
- `GET /dashboard` - User dashboard (if logged in)
- `GET /about` - About page
- `GET /delete/<sno>` - Delete employee
- `GET /update/<sno>` - Update employee page
- `POST /update/<sno>` - Submit employee update

## Validation Rules

### Registration Validation

All validation is performed server-side (Flask backend):

1. **Name**: Required, cannot be empty
2. **Email**: Required, cannot be empty, must be unique
3. **Password**: Required, minimum 6 characters

### Error Messages

- "Name is required" - If name field is empty
- "Email is required" - If email field is empty
- "Password is required" - If password field is empty
- "Password must be at least 6 characters" - If password is less than 6 characters
- "Email already registered" - If email already exists in database

## Database Schema

### Employees Table

```sql
CREATE TABLE employees (
    sno INTEGER PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    email VARCHAR(500) NOT NULL UNIQUE,
    password VARCHAR(500) NOT NULL
);
```

## Security Features

- Server-side validation for all user inputs
- Unique email constraint at database level
- SQLAlchemy ORM for SQL injection prevention
- Session management for user authentication

## Design Features

- **Gradient Background**: Professional purple-to-violet gradient
- **Card-based Forms**: Modern card design with shadows
- **Responsive Layout**: Mobile-friendly design
- **Smooth Animations**: Hover effects and transitions
- **Flash Messages**: User-friendly error and success notifications

## Author

Kushagra-SethG

## License

MIT License
