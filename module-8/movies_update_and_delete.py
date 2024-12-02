import mysql.connector

# Connect to the database
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",  
        password="password", 
        database="movies"  
    )

# Establish connection
conn = connect_to_database()
cursor = conn.cursor()

def show_films(cursor, title):
    # Execute the query to select film data
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
    
    