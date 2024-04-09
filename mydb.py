# Install MySQL if you do not have it: https://www.w3schools.com/mysql/mysql_install_windows.asp#:~:text=The%20simplest%20and%20recommended%20method,%2D8.0.23.msi%20.
# pip install mysql
# pip install mysql-connector-python
# IF THE PREVIOUS CONNECTOR DOES NOT WORK, USE: pip install mysql-connector
# now run on your terminal: python mydb.py
# if "Db set up!" appears on your terminal, all worked well
# A video on how to set up django with mySQL is available here: https://www.youtube.com/watch?v=t10QcFx7d5k
import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Connect to the PostgreSQL database server
conn = psycopg2.connect(
    host='localhost',
    user='postgres',  # Default user for PostgreSQL
    password=os.environ.get('POSTGRES_PASSWORD'),
    port='5432',  # Default port for PostgreSQL
)

# Create a cursor object
cursor = conn.cursor()

# Disable autocommit mode
conn.autocommit = True

# Create a new database named 'pollnpostgres'
try:
    cursor.execute("CREATE DATABASE pollnpostgres")
    print("Database 'pollnpostgres' created successfully!")
except psycopg2.Error as e:
    print(f"Error creating database: {e}")

# Close communication with the PostgreSQL database server
cursor.close()
conn.close()
