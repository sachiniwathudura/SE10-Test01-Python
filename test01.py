import mysql.connector
from mysql.connector import Error

def create_connection():
    """Creates a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',          # Replace with your host if different
            user='root',      # Replace with your MySQL username
            password='Ijse@1234',  # Replace with your MySQL password
            database='test01Python'   # Replace with your MySQL database name
        )
        if connection.is_connected():
            print("Successfully connected to the database")
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def create_table(connection):
    """Creates a table if it doesn't exist."""
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(100) NOT NULL,
        last_name VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE,
        password VARCHAR(100) NOT NULL
    )
    '''
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_query)
        print("Table 'users' is ready.")
    except Error as e:
        print(f"Failed to create table: {e}")

def get_user_input():
    """Gets user input from the console."""
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    return first_name, last_name, email, password

def save_user_to_db(connection, first_name, last_name, email, password):
    """Saves the user details into the database."""
    insert_query = '''
    INSERT INTO users (first_name, last_name, email, password)
    VALUES (%s, %s, %s, %s)
    '''
    try:
        cursor = connection.cursor()
        cursor.execute(insert_query, (first_name, last_name, email, password))
        connection.commit()
        print("User saved successfully!")
    except Error as e:
        print(f"Failed to insert user: {e}")

def main():
    """Main function to run the program."""
    connection = create_connection()
    if connection is not None:
        create_table(connection)
        first_name, last_name, email, password = get_user_input()
        save_user_to_db(connection, first_name, last_name, email, password)
        connection.close()
    else:
        print("Connection to database failed.")

if __name__ == "__main__":
    main()
