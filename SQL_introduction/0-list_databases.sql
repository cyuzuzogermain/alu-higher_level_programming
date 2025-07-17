--Query to display all the databases
import mysql.connector

# Replace these with your actual MySQL credentials
config = {
    'user': 'root',
    'password': 'your_password',
    'host': 'localhost',
    'port': 3306
}

try:
    # Connect to the MySQL server
    connection = mysql.connector.connect(**config)

    # Create a cursor object
    cursor = connection.cursor()

    # Execute the query to list all databases
    cursor.execute("SHOW DATABASES;")

    print("Available Databases:")
    for (db,) in cursor:
        print(f" - {db}")

except mysql.connector.Error as err:
    print(f"❌ Error: {err}")

finally:
    # Clean up
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
