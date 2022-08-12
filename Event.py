import sqlite3
import datetime as dt


class event:
    _event = []
    _con = sqlite3.connect('mkvt.db')
    _cur = _con.cursor()

    def close(self):
        self._con.close()


    def create(self):
        # self._event.append({'datetime': datetime, 'message': message})
        self._cur.execute('''DROP TABLE event;''')
        self._cur.execute('''CREATE TABLE event
                        (message_id TEXT NOT NULL,
                        datetime DATETIME NOT NULL, 
                        event TEXT NOT NULL);''')


    def insert(self, message_id, datetime, message):
        self._con.execute(f"INSERT INTO event VALUES ('{message_id}', '{datetime}', '{message}');")
        self._con.commit()


    def select(self):
        # res = _cur.execute('SELECT count(rowid) FROM event')
        res = self._cur.execute('SELECT * FROM event ORDER BY datetime;')
        print('===select')
        result = res.fetchall()
        print(result)
        return result


    def delete(self, id):
        # res = _cur.execute('SELECT count(rowid) FROM event')
        res = self._cur.execute('DELETE FROM event WHERE rowid = ?;', (id,))
        self._con.commit()


    def getByDate(self, date):
        res = self._cur.execute('SELECT * FROM event WHERE DATE(datetime) = ? ORDER BY datetime;', (date,))
        print('===select')
        result = res.fetchall()
        print(result)
        return result


    def getEventsToday(self):
        today = dt.datetime.today()
        curDate = today.strftime('%Y-%m-%d')
        # curDate = "2022-09-03"
        events = self.getByDate(curDate)
        events = self.select()
        # return events
        result = ''
        for event in events:
            strdt = dt.datetime.strptime(event[1], '%Y-%m-%d %H:%M:%S')
            dtEvent = strdt.strftime('%d/%m %H:%M')
            string = f'<b>{dtEvent}</b> - {event[2]}'
            print(string)
            result += f'\n     {string}'
        if result == '':
            result = '=пусто='
        return result

    # def insert_varibles_into_table(datetime, message):
        # try:
        #     connection = mysql.connector.connect(host = 'localhost',
        #                                          port = '3306',
        #                                          database = 'event-malavita',
        #                                          user = 'root',
        #                                          password = '')
        #     cursor = connection.cursor()
        #     mySql_insert_query = """INSERT INTO event (datetime, message) VALUES (%s, %s) """

        #     record = (datetime, message)
        #     cursor.execute(mySql_insert_query, record)
        #     connection.commit()
        #     print("Record inserted successfully into Laptop table")

        # except mysql.connector.Error as error:
        #     print("Failed to insert into MySQL table {}".format(error))

        # finally:
        #     if connection.is_connected():
        #         cursor.close()
        #         connection.close()
        #         print("MySQL connection is closed")

# Event = event()
# Event.create()