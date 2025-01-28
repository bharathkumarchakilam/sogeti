import mysql.connector

# Test connection
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Bharath@2647",
        )
    if connection.is_connected():
        print("Connection successful!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
