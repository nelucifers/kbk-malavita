import mysql.connector
from DatetimeParser import parser
from Event import event


def insert_varibles_into_table(datetime, message):
    try:
        connection = mysql.connector.connect(host = 'localhost',
                                             port = '3306',
                                             database = 'event-malavita',
                                             user = 'root',
                                             password = '')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO event (datetime, message) VALUES (%s, %s) """

        record = (datetime, message)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("Record inserted successfully into Laptop table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            

def test():
    dp = parser()
    testMessages = ('завтра в 12:30 тест111', 
                    'послезавтра в 12 часов lskdsdl jsalfsdk asdfkasdlkfj', 
                    '13.08.2022 в 12:30 тест222', 
                    '13 июля 2022 в 12:30 lskdsdl jsalfsdk asdfkasdlkfj alskd lkasdjfl sd12 22'
    )
    
    for msg in testMessages:
        eventNew = event()
        dp.setMessage(msg)
        datetime = dp.getDateTime()
        message = dp._message
        eventNew.add(datetime, message)
        insert_varibles_into_table(datetime, message)

        print(msg)
        # print(dp.getDate())
        # print(dp.getTime())
        print(datetime)
        print(message)
        print('===============')
        print(event._event)




test()