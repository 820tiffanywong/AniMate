import sys
import os
import psycopg2
sys.path.append('..')
from flask import Flask, render_template, request, flash, url_for, redirect
from forms import RegistrationForm
from flask_sqlalchemy import SQLAlchemy
from user import User
from postgres import Connector


cur = Connector()

# # Add the parent directory to the Python path
# sys.path.append('..')
# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory of the current directory
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
app = Flask(__name__)
app.config['SECRET_KEY']='12345'
db = Connector()
user = User()
@app.route("/")
@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":

        # collect login info from user
        username = request.form.get("username")
        password = request.form.get("password")
        print(username, password)
        
        # check if already on database
        query = f"SELECT 1 FROM username WHERE username = '{username}';"
        cur.execute(query)
        current_users = cur.fetchall()

        # let user know username is taken
        if len(current_users > 0):
            print("USERNAME TAKEN")
        
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        try:
            fname = request.form.get("fname")
            lname = request.form.get("lname")
            username = request.form.get("username")
            password = request.form.get("password")
            confirm_password = request.form.get("confirm_password")
            print(fname, lname, username, password, confirm_password)  # Check form data
            # Process form data (e.g., insert into database)
            if password == confirm_password:
            # Process user registration
            # Add your database logic here
                user.create_user(username, fname, lname, password)
                print("User registered successfully!")
            else:
                print("Passwords do not match. Please try again.")
            
            # return 'Form submitted successfully'  # Placeholder response
        except Exception as e:
            print(f'An error occurred: {e}')  # Debugging statement
            return f'An error occurred: {e}'
   
    """
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    """
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    #form = User.login_form()
    form = LoginForm()
    username = request.form['username']
    password = request.form['password']
    
    user = User(username)  # Instantiate User class
    message = user.verify_user(username, password)  # Validate user
    if form.validate_on_submit():
        # Check if the user credentials are valid (you need to implement this)
        # For demonstration, let's assume the login is successful
        # Redirect to the anime swiping page after successful login
        return redirect(url_for('login'))
    return render_template('login.html', title='Login', form=form, message=message)

@app.route("/validate", methods=['POST'])  # Bind to a route and specify accepted methods
def validate_username(self):
    username = request.form['username']
    password = request.form['password']
    
    user = User(username)  # Instantiate User class
    message = user.verify_user(username, password)  # Validate user
    
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)