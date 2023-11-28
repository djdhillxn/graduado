# Graduate School Application Tracker

## Description
Graduate School Application Tracker is a Flask-based web application designed to help users track and manage their applications to various graduate programs. It offers features like adding, editing, and deleting application records, user authentication, and a dashboard for easy management.

## Features
- User registration and login
- Dashboard for tracking graduate school applications
- Add, edit, and delete functionality for application records
- Responsive design for various devices

## Installation

### Prerequisites
- Python 3.x
- pip (Python package manager)
- Virtual environment (recommended)

### Clone the Repository
First, clone the repository to your local machine:
```bash
git clone https://github.com/your-username/graduado.git
cd graduado
```

### Set Up a Virtual Environment
Create a virtual environment to manage the dependencies:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scriptsctivate`
```

### Install Dependencies
Install all the required packages:
```bash
pip install -r requirements.txt
```

### Environment Variables
Set up the necessary environment variables. Create a `.env` file in the root directory and add the following (replace values as needed):
```env
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///db.sqlite  # or your database URI
FLASK_APP=run.py
FLASK_ENV=development  # Set to 'production' in a production environment
```

### Initialize the Database
Run the following commands to set up your database:
```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

### Running the Application
Start the server with:
```bash
flask run
```
Access the application through `http://127.0.0.1:5000/` in your web browser.

## Usage
After starting the application, you can:
- Register a new user account.
- Log in with your credentials.
- Add, view, edit, or delete your graduate school applications via the dashboard.

## Deployment
For deploying to a production environment, additional setup for a production-ready server like Gunicorn and a web server like Nginx is recommended.

## Contributing
Contributions to the Graduate School Application Tracker are welcome. Please ensure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
