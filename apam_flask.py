import psycopg2
from flask import Flask, request


app = Flask(__name__)

# Connect to the database
conn = psycopg2.connect(database="Skin_care", user="postgres", password="christina@53", host="localhost", port="5432")
cur = conn.cursor()

# Create the table to store the user's data
cur.execute("CREATE TABLE IF NOT EXISTS mytable (id serial PRIMARY KEY, name varchar(50),Age integer,sex varchar(50), email varchar(50),location varchar(50),phone_number integer,skin_condition varchar(50),medical_condition varchar(50),occupation varchar(50),guardians_name varchar(50));")

# Handle the form submission
@app.route('/submit_form.py', methods=['POST'])
def submit_form():
    name = request.form['name']
    Age = request.form['age']
    sex = request.form['sex']
    email = request.form['email']
    location = request.form['location']
    phone_number = request.form['phone_number']
    skin_condition = request.form['skin_condition']
    medical_condition = request.form['medical_condition']
    occupation = request.form['occupation']
    guardians_name = request.form['guardians_name']
    
    cur.execute("INSERT INTO mytable (name,Age,sex, email,location,phone_number,skin_condition,medical_condition,occupation,guardians_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", (name,Age,sex, email,location,phone_number,skin_condition,medical_condition,occupation,guardians_name))
    conn.commit()

    return 'Data successfully saved to database!'

# Close the database connection
cur.close()
conn.close()

if __name__ == '__main__':
    app.run(debug=False)