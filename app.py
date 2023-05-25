#same directory crete two files 1.app.py , 2.db.py
from flask import Flask, request
from db import cnx, create_table

app = Flask(__name__)

# Create the table if it doesn't exist
create_table()

# Render the HTML form
@app.route('/', methods=['GET'])
def index():
    return '''
        <html>
        <head>
            <title>Data Entry Form</title>
        </head>
        <body>
            <h1>Data Entry Form</h1>

            <form action="/" method="POST">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required><br><br>

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required><br><br>
                <label for="message">Message:</label>
                <textarea id="message" name="message" rows="4" cols="50"></textarea><br><br>

                <label for="gender">Gender:</label>
                <input type="radio" id="male" name="gender" value="male" required>
                <label for="male">Male</label>
                <input type="radio" id="female" name="gender" value="female" required>
                <label for="female">Female</label><br><br>

                <label for="interests">Interests:</label>
                <input type="checkbox" id="sports" name="interests" value="sports">
                <label for="sports">Sports</label>
                <input type="checkbox" id="music" name="interests" value="music">
                <label for="music">Music</label>
                <input type="checkbox" id="reading" name="interests" value="reading">
                <label for="reading">Reading</label><br><br>

                <input type="submit" value="Submit">
            </form>
        </body>
        </html>
    '''

# Handle form submission
@app.route('/', methods=['POST'])
def submit_form():
    # Retrieve form data
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    gender = request.form['gender']
    interests = request.form.getlist('interests')

    # Execute SQL INSERT statement
    cursor = cnx.cursor()
    sql = "INSERT INTO users (name, email, message, gender, interests) VALUES (%s, %s, %s, %s, %s)"
    values = (name, email, message, gender, ', '.join(interests))

    cursor.execute(sql, values)
    cnx.commit()

    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
