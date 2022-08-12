import datetime as dt
import asyncio
import telegram
from telegram.ext import Job
from time import sleep
from DatetimeParser import parser
from Event import event

_hour = 17
_minute = 50
TOKEN = '5048220651:AAET4h_9_iq0J5qcsmeUUj9qnX8EhJ_0okc'
CHAT_ID = '5136585077'
bot = telegram.Bot(TOKEN)

_cEvent = event()

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
        _cEvent.insert(datetime, message)
        print(msg)
        # print(dp.getDate())
        # print(dp.getTime())
        print(datetime)
        print(message)
        print('===============')
        print(event._event)

    _cEvent.select()


def getEventsToday():
    today = dt.datetime.today()
    curDate = today.strftime('%Y-%m-%d')
    curDate = "2022-09-03"
    events = _cEvent.getByDate(curDate)
    events = _cEvent.select()
    # return events
    result = ''
    for event in events:
        strdt = dt.datetime.strptime(event[0], '%Y-%m-%d %H:%M:%S')
        # numMonth = strdt.strftime('%m')
        # month = parser.numToMonth(numMonth)
        # day = strdt.strftime('%d')
        # time = strdt.strftime('%H:%M')
        # dtEvent = f'{day}/{numMonth} {time}'
        dtEvent = strdt.strftime('%d/%m %H:%M')
        string = f'<b>{dtEvent}</b> - {event[1]}'
        print(string)
        result += f'\n     {string}'
    if result == '':
        result = '=пусто='
    return result


# async def get_me():
#     async with bot:
#         print(await bot.get_me())
# asyncio.run(get_me())

async def send(message, parse_mode='HTML'):
    async with bot:
        await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode=parse_mode)


async def main():

    # await send('test')

    # async with bot:
    #     await bot.send_message(chat_id=CHAT_ID, text='testr')
    
    # test()
    # delete(1)
    # delete(2)
    _cEvent.select()
    # eventNew.create()

    events = getEventsToday()
    # string = ''
    # for event in events:
    #     strdt = dt.datetime.strptime(event[0], '%Y-%m-%d %H:%M:%S')
    #     dtEvent = strdt.strftime('%d.%m.%Y %H:%M')
    #     string += dtEvent + '-' + event[1] + f'\n'
    #     print(string)
    # await send(string)
    await send(f'<pre>События на сегодня:</pre>' + events)

    # while True:
    #     # now = dt.datetime.now()
    #     # if curHour == 0 and curHinute == 0:
    #     #     getEventsToday()

    #     now = dt.datetime.now()
    #     curHour = now.hour
    #     curHinute = now.minute
    #     # print(f'Time: {_hour}:{_minute}')
    #     # if curHour == _hour and curHinute == _minute:
    #     if curHour == 10 and curHinute == 50:
    #         events = getEventsToday()
    #         sleep(60)
    #         await send(events)
    #     sleep(30)

    _cEvent.close()


if __name__ == '__main__':
    asyncio.run(main())