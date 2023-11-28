# Graduate School Application Tracker

## Description

Graduate School Application Tracker is a Flask-based web application designed to help users track and manage their applications to various graduate programs. It features user authentication, a dashboard for managing applications, and functionality for tracking letters of recommendation and personal statements.

## Tech Stack
- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**: HTML(Jinja2), Bootstrap, JavaScript
- **Libraries/Frameworks**: Flask-WTF, Flask-SQLAlchemy, Flask-Migrate, Flask-Login

## Installation

### Prerequisites
- Python 3.x
- pip3 

### Clone the Repository
First, clone to local machine:
```bash
git clone https://github.com/djdhillxn/graduado.git
cd graduado
```

### Install Dependencies
```bash
pip3 install -r requirements.txt
```

### Environment Variables
Set up the necessary environment variables. Create a `.env` file in the root directory and add the following (replace values as needed):
```env
SECRET_KEY=your_secret_key
```

### Initialize the Database
Before initializing the database, make sure the \`migrations\` folder is present. If not, run:
```bash
flask db init
```

Then, run the following commands to set up your database:
```bash
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
- Add, view, edit, or delete your graduate school applications, letters of recommendation, and personal statements via the dashboard.

## Future Scope
Following features and improvements could be considered to enhance its functionality and user experience:
- **Customizable Dashboard:** Prioritize certain applications or deadlines, document upload and storage.
- **Production Environment Deployment:** Heroku app.

## Contributing
Contributions are more than welcome.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
