import mysql.connector

def create_user(name, email, age):
    connection = mysql.connector.connect(host="localhost", user="root", password="Bharath@2647", database="test_db")
    cursor = connection.cursor()
    
    query = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
    values = (name, email, age)
    cursor.execute(query, values)
    
    connection.commit()
    print(f"User {name} added successfully!")
    cursor.close()
    connection.close()

# Example Usage
create_user("John Doe", "john@example.com", 30)
