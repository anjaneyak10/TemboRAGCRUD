import os
import psycopg2

class SearchDao:
    # This function executes the query and returns the result.
    def execute_query(self, query):
        # will get the DATABASE_URL value present in .env file
        url = os.getenv("DATABASE_URL")
        print(query)
        conn = psycopg2.connect(url)
        cursor = conn.cursor()
        cursor.execute(query)
        x= cursor.fetchall()
        cursor.close()
        conn.close()
        return x
