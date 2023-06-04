from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
# @app.route('/home')
def home():
    return render_template("base.html")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Naira_land_Clone/storage.db'
db = SQLAlchemy(app)

# Define the models (User, Post, Comment, Group, Interest) here

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Process the registration form data
        # Create a new User object and add it to the database
        # Redirect the user to the login page or their profile
        return redirect(url_for('login'))
    return render_template('register.html')

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Process the login form data
        # Validate the user credentials
        # Redirect the user to their profile
        return redirect(url_for('profile'))
    return render_template('login.html')

# Route for user profile
@app.route('/profile')
def profile():
    # Get the currently logged-in user
    # Retrieve user information from the database
    # Display the user profile with their details, posts, etc.
    return render_template('profile.html')

# Route for creating a new post
@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        # Process the post creation form data
        # Create a new Post object and add it to the database
        # Redirect the user to their profile or the post details page
        return redirect(url_for('profile'))
    return render_template('create_post.html')

# Route for joining a group
@app.route('/join_group/<group_id>', methods=['POST'])
def join_group(group_id):
    # Process the group join request
    # Add the user to the specified group in the database
    # Redirect the user to their profile or the group details page
    return redirect(url_for('profile'))

if __name__ == '__main__':
    app.run(debug=True)
