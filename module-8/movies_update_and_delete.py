import mysql.connector
from mysql.connector import Error

# Connect to the database
def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",  
            password="password",  
            database="movies"  
        )
        if conn.is_connected():
            print("Connected to the database")
            return conn
    except Error as e:
        print(f"Error: {e}")
        return None

# Function to display films
def show_films(cursor, title):
    query = """
    SELECT film_name AS Name, genre_name AS Genre, studio_name AS 'Studio Name' 
    FROM film 
    INNER JOIN genre ON film.genre_id = genre.genre_id 
    INNER JOIN studio ON film.studio_id = studio.studio_id
    """
    cursor.execute(query)
    results = cursor.fetchall()

    # Display the results with the given title
    print(title)
    print(f"{'Name':<30}{'Genre':<20}{'Studio Name'}")
    print("=" * 70)
    for row in results:
        print(f"{row[0]:<30}{row[1]:<20}{row[2]}")
    print("\n")

# Function to insert a new film
def insert_film(cursor, conn):
    try:
        insert_query = """
        INSERT INTO film (film_name, genre_id, studio_id, film_releaseDate) 
        VALUES (%s, %s, %s, %s)
        """
        new_film = ('Inception', 1, 2, '2010-07-16')  # Add a release date for the film
        cursor.execute(insert_query, new_film)
        conn.commit()
        print("New film 'Inception' inserted successfully.\n")
    except Error as e:
        print(f"Error inserting film: {e}")
        conn.rollback()

# Function to update the genre of a film
def update_film_genre(cursor, conn):
    try:
        update_query = """
        UPDATE film 
        SET genre_id = (SELECT genre_id FROM genre WHERE genre_name = 'Horror')
        WHERE film_name = 'Alien'
        """
        cursor.execute(update_query)
        conn.commit()
        print("Film 'Alien' genre updated to Horror.\n")
    except Error as e:
        print(f"Error updating film genre: {e}")
        conn.rollback()

# Function to delete a film
def delete_film(cursor, conn):
    try:
        delete_query = "DELETE FROM film WHERE film_name = 'Gladiator'"
        cursor.execute(delete_query)
        conn.commit()
        print("Film 'Gladiator' deleted.\n")
    except Error as e:
        print(f"Error deleting film: {e}")
        conn.rollback()

# Main function to tie everything together
def main():
    # Establish connection
    conn = connect_to_database()
    if conn is None:
        return  # Exit if connection failed
    
    cursor = conn.cursor()

    # Display films before any modifications
    show_films(cursor, "DISPLAYING FILMS")

    # Insert a new film
    insert_film(cursor, conn)

    # Display films after insertion
    show_films(cursor, "DISPLAYING FILMS AFTER INSERTION")

    # Update genre of Alien to Horror
    update_film_genre(cursor, conn)

    # Display films after update
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")

    # Delete the film Gladiator
    delete_film(cursor, conn)

    # Display films after deletion
    show_films(cursor, "DISPLAYING FILMS AFTER DELETION")

    # Close the connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()