
import psycopg2

# Connect to the database
conn = psycopg2.connect(database="Skin_care", user="postgres", password="christina@53", host="localhost", port="5432")
cur = conn.cursor()

# Create the table to store the user's data
cur.execute("CREATE TABLE IF NOT EXISTS mytable (id serial PRIMARY KEY, name varchar(50),Age integer,sex varchar(50), email varchar(50),location varchar(50),phone_number integer,skin_condition varchar(50),medical_condition varchar(50),occupation varchar(50),guardians_name varchar(50));")

# Retrieve data from the form and insert it into the database
name = input("Enter your name: ")
Age=input("enter your age:")
sex=input("enter your sex:")
email = input("Enter your email: ")
location=input("enter your location:")
phone_number=input("enter your phone_number:")
skin_condition=input("enter your skin_condition:")
medical_condition=input("enter your medical_condition:")
occupation=input("enter your occupation:")
guardians_name=input("enter guardians_name:")

cur.execute("INSERT INTO mytable (name,Age,sex, email,location,phone_number,skin_condition,medical_condition,occupation,guardians_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", (name,Age,sex, email,location,phone_number,skin_condition,medical_condition,occupation,guardians_name))
conn.commit()

# Close the database connection
cur.close()
conn.close()
