import mysql.connector
from mysql.connector import Error  # Ensure Error is imported

def create_database():
    connection = None  # Initialize connection variable
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='Abou',  # Use your username
            password='Newabou22'  # Use your correct password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        
    except mysql.connector.Error as e:  # Handle mysql.connector.Error
        print(f"Error: {e}")
    
    finally:
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
