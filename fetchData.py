import SQLqueries
import dbCredentials
from mysql.connector import connect, Error

my_queries = SQLqueries.queries
db_connection = dbCredentials.credentials

#Fetch data from MySQL DB
def mySQL_query(query,db_params):
    try:
        with connect(**db_params) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
    except Error as e:
        print(e)

#Replace query with data
for d in my_queries:
    for value in d:
        d[value] = mySQL_query(d[value],db_connection)

my_data = my_queries
