import mysql.connector

# Connect to MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',      
    password='password',  
    database='movies'  
)

cursor = connection.cursor()

# 1. Query to select all fields from the 'studio' table
print("1. All fields from the 'studio' table:")
cursor.execute("SELECT * FROM studio;")
studios = cursor.fetchall()
for row in studios:
    print(row)

# 2. Query to select all fields from the 'genre' table
print("\n2. All fields from the 'genre' table:")
cursor.execute("SELECT * FROM genre;")
genres = cursor.fetchall()
for row in genres:
    print(row)

# 3. Query to select movie names with a runtime of less than 2 hours
print("\n3. Movie names with a runtime of less than 2 hours:")
cursor.execute("SELECT movie_name FROM movies WHERE runtime < 120;")
short_movies = cursor.fetchall()
for row in short_movies:
    print(row)

# Query 4: Get a list of film names and directors grouped by director
query4 = """
SELECT director, GROUP_CONCAT(movie_name ORDER BY movie_name ASC) AS movie_names
FROM movies 
GROUP BY director;
"""
cursor.execute(query4)
print("\nQuery 4: List of film names and directors grouped by director")
for row in cursor.fetchall():
    print(row)