from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/profile_pictures'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle registration form submission
        username = request.form['username']
        # Store the user's profile picture
        file = request.files['profile_picture']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Save the user's registration details to a database or file
        # (you'll need to set up a database or file storage separately)
        # Redirect the user to the login page
        return redirect(url_for('login'))
    return render_template('register.html')

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login form submission
        username = request.form['username']
        password = request.form['password']
        # Validate the username and password against the stored data
        # (you'll need to implement this logic separately)
        # If the login is successful, redirect the user to their profile page
        return redirect(url_for('profile', username=username))
    return render_template('login.html')

# Route for the user's profile page
@app.route('/profile/<username>')
def profile(username):
    # Retrieve the user's profile picture from the database or file storage
    profile_picture = os.path.join(app.config['UPLOAD_FOLDER'], f'{username}.jpg')
    return render_template('profile.html', username=username, profile_picture=profile_picture)

if __name__ == '__main__':
    app.run(debug=True)
