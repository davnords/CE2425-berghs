import psycopg2
from psycopg2 import sql

# Database connection parameters
db_url = "postgresql://neondb_owner:3g5FJbUcReZO@ep-noisy-sky-a2xtf0fp.eu-central-1.aws.neon.tech/neondb?sslmode=require"


def create_user(name, email): 
    try:
        # Establish the connection
        conn = psycopg2.connect(db_url)
        cursor = conn.cursor()
        print("Database connection established.")

        # Insert data into the User table (excluding the 'id' column)
        insert_query = """
            INSERT INTO "User" (name, email, created_at)
            VALUES (%s, %s, NOW())
        """
        data = (name, email)  # Replace with actual data

        # Execute the query
        cursor.execute(insert_query, data)
        conn.commit()
        print("Data inserted successfully into the User table.")

    except psycopg2.Error as e:
        print(f"Error: {e}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        print("Database connection closed.")
