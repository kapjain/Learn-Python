import psycopg2

try:
    conn = psycopg2.connect(host="localhost",database="locallibrary", user="postgres", password="cwise",port='5432')
    print ("Connecting to database %s successful...")
    cur = conn.cursor()
    print('PostgreSQL database version:')
    cur.execute('SELECT version()')
    
    # display the PostgreSQL database server version
    db_version = cur.fetchone()
    print(db_version)
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print('Database connection closed.')
    # close the communication with the PostgreSQL
    

# import psycopg2        
# from django.conf import settings        
#         selected_db_conn = psycopg2.connect(
#             database = settings.DATABASES[selected_db]['NAME'], 
#             host = settings.DATABASES[selected_db]['HOST'] or 'localhost', 
#             port = settings.DATABASES[selected_db]['PORT'] or '5432', 
#             user = settings.DATABASES[selected_db]['USER'], 
#             password = settings.DATABASES[selected_db]['PASSWORD'])