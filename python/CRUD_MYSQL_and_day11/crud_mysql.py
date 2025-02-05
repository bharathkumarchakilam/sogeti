import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",  # Change to your MySQL server host
    user="root",       # Change to your MySQL username
    password="Bharath@2647",  # Replace with your MySQL password
    database="test_db"
)

if connection.is_connected():
    print("Connected to MySQL")
else:
    print("Connection failed")

connection.close()

#inserting
def create_user(name, email, age):
    connection = mysql.connector.connect(host="localhost", user="root", password="Bharath@2647", database="test_db")
    cursor = connection.cursor()
    
    #inserting
    query = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
    values = (name, email, age)
    cursor.execute(query, values)
    
    connection.commit()
    print(f"User {name} added successfully!")
    cursor.close()
    connection.close()

#printing
def fetch_users():
    connection = mysql.connector.connect(host="localhost", user="root", password="Bharath@2647", database="test_db")
    cursor = connection.cursor()
    
    query = "SELECT * FROM users"
    cursor.execute(query)
    results = cursor.fetchall()
    
    for row in results:
        print(row)
    
    cursor.close()
    connection.close()

# Example Usage
fetch_users()

#updating
def update_user(user_id, name, email, age):
    connection = mysql.connector.connect(host="localhost", user="root", password="Bharath@2647", database="test_db")
    cursor = connection.cursor()
    
    query = "UPDATE users SET name=%s, email=%s, age=%s WHERE id=%s"
    values = (name, email, age, user_id)
    cursor.execute(query, values)
    
    connection.commit()
    print(f"User {user_id} updated successfully!")
    cursor.close()
    connection.close()

# Example Usage
update_user(1, "Johnathan Doe", "johnathan@example.com", 35)

#deleting
def delete_user(user_id):
    connection = mysql.connector.connect(host="localhost", user="root", password="Bharath@2647", database="test_db")
    cursor = connection.cursor()
    
    query = "DELETE FROM users WHERE id=%s"
    cursor.execute(query, (user_id,))
    
    connection.commit()
    print(f"User {user_id} deleted successfully!")
    cursor.close()
    connection.close()

# Example Usage
delete_user(1)



