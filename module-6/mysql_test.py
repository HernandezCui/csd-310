import mysql.connector
from mysql.connector import Error

# Database connection parameters
config = {
    'user': 'root',        
    'password': 'password', 
    'host': '127.0.0.1',        
    'database': 'movies',       
}

try:
    # Establish a connection
    connection = mysql.connector.connect(**config)
    
    # Check if the connection was successful
    if connection.is_connected():
        print("Connection successful!")
    else:
        print("Failed to connect.")
except Error as err:
    # Catch any errors and print them
    print(f"Error: {err}")
finally:
    # Close the connection if it's open
    if connection.is_connected():
        connection.close()
        print("Connection closed.")