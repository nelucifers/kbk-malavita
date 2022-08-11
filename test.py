import datetime as dt
from time import sleep
from DatetimeParser import parser
from Event import event
import telegram_send

_hour = 17
_minute = 50


def test():
    dp = parser()
    testMessages = ('завтра в 12:55 тест111', 
                    'послезавтра в 12 часов lskdsdl jsalfsdk asdfkasdlkfj', 
                    '13.10.2022 в 10:45 тест222', 
                    '3 сентября 2022 в 16:30 lskdsdl jsalfsdk asdfkasdlkfj alskd lkasdjfl sd12 22'
    )

    for msg in testMessages:
        dp.setMessage(msg)
        datetime = dp.getDateTime()
        message = dp._message
        cEvent.insert(datetime, message)
        print(msg)
        # print(dp.getDate())
        # print(dp.getTime())
        print(datetime)
        print(message)
        print('===============')
        print(event._event)

    cEvent.select()


def getEventsToday():
    today = dt.datetime.today()
    curDate = today.strftime('%Y-%m-%d')
    curDate = "2022-09-03"
    events = cEvent.getByDate(curDate)
    events = cEvent.select()
    result = ''
    for event in events:
        strdt = dt.datetime.strptime(event[0], '%Y-%m-%d %H:%M:%S')
        dtEvent = strdt.strftime('%d.%m.%Y %H:%M')
        string = dtEvent + '-' + event[1]
        print(string)
        result += f'\n{string}'
    return result


cEvent = event()
# test()
# delete(1)
# delete(2)
cEvent.select()
# eventNew.create()


while True:
    # now = dt.datetime.now()
    # if curHour == 0 and curHinute == 0:
    #     getEventsToday()

    now = dt.datetime.now()
    curHour = now.hour
    curHinute = now.minute
    # print(f'Time: {_hour}:{_minute}')
    if curHour == _hour and curHinute == _minute:
        events = getEventsToday()
        sleep(60)
        telegram_send.send(messages=events)
    sleep(30)


cEvent.close()