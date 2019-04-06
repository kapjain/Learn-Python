import psycopg2

try:
    conn = psycopg2.connect(host="localhost",database="railway_db", user="postgres", password="cwise",port='5432')
    print ("Connecting to database %s successful...")
    cur = conn.cursor()
    query = """SELECT pd.name, pd.age, pd.gender ,pd.with_child, td.ticket_nbr, td.date_of_journey, bt.berth_type, ts.status_code, coach.coach_nbr
        FROM passanger_detail pd
        INNER JOIN ticket_detail td ON pd.ticket_id = td.id
        LEFT OUTER JOIN berth_type bt ON td.berth_type_id = bt.id
        LEFT OUTER JOIN ticket_status ts ON td.status_id = ts.id
        LEFT OUTER JOIN coach ON td.coach_id = coach.id"""
    cur.execute(query)
    
    # display the PostgreSQL database server version
    passanger_detail_list = cur.fetchall()
    print(passanger_detail_list)
    response_list=[]
    for passanger_detail in passanger_detail_list:
        temp_dict = {}
        temp_dict["NAME"] = passanger_detail[0]
        temp_dict["AGE"] = passanger_detail[1]
        temp_dict["GENDER"] = passanger_detail[2]
        temp_dict["WITH_CHILD"] = passanger_detail[3]
        temp_dict["TICKET_NBR"] = passanger_detail[4]
        temp_dict["DATE_OF_JOURNEY"] = passanger_detail[5]
        temp_dict["BERTH_TYPE"] = passanger_detail[6]
        temp_dict["STATUS_CODE"] = passanger_detail[7]
        temp_dict["COACH_NBR"] = passanger_detail[8]
        response_list.append(temp_dict)
    
    print(response_list)
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print('Database connection closed.')
    # close the communication with the PostgreSQL