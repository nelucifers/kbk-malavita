import datetime
import re


class DatetimeParser():

    MESSAGE = ''

    def setMessage(self, message):
        self.MESSAGE = message

    # def getMonthNumber(self, message):
    #     months = ['янв', 'фев', 'мар', 'апр', 'мая' , 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
    #     for month in months:
    #         if month in message:
    #             number = months.index(month) + 1
    #             result = str(number)
    #             if number < 10:
    #                 result = "0" + result
    #             return result

    def monthToNum(self, shortMonth):
        return {
                'янв': '01',
                'фев': '02',
                'мар': '03',
                'апр': '04',
                'мая': '05',
                'июн': '06',
                'июл': '07',
                'авг': '08',
                'сен': '09', 
                'окт': '10',
                'ноя': '11',
                'дек': '12'
        }[shortMonth]


    def getDate(self):
        message = self.MESSAGE

        date = datetime.date.today()
        result = ''
        if message.find('послезавтра') >= 0:
            result = date + datetime.timedelta(days=2)
        elif message.find('завтра') >= 0:
            result = date + datetime.timedelta(days=1)
        elif message.find('сегодня') >= 0:
            result = date

        if result == '':
            pattern = r'^(\d{1,2})\.?(\d{1,2})?\s?((янв|фев|мар|июн|июл|авг|сен|окт|ноя|дек).+?)?\s?\.?(\d{4})?'
            matches = re.search(pattern, message)
            # print(matches)
            if(matches != None):
                # length = len(matches.group(0))
                # message = message[length:]
                # print(message)
                result = matches.group(1) + '.'
                if matches.group(2):
                    result += matches.group(2) + '.'
                elif(matches.group(4)):
                    month = matches.group(4)
                    if month.isdigit():
                        result += month + '.'
                    else:
                        monthNumber = self.monthToNum(month)
                        # print(monthNumber)
                        result += str(monthNumber) + '.'
                if matches.group(5):
                    result += matches.group(5)
                else:
                     result += date.year

        return result


    def getTime(self):
        message = self.MESSAGE

        result = ''
        pattern = r'(\d{1,2})([:-](\d{1,2})|\s?ч(\.|(ас\w+))?)'
        matches = re.search(pattern, message)
        print(matches)

        if(matches != None):
            length = matches.span(0)[1]
            message = message[length:].strip()
            print(message)
            # message = message.replace(matches.group(0), '')
            result = matches.group(1) + ':'
            if matches.group(3):
                result += matches.group(3)
            else:
                result += '00'
        
        return result
    

    def test(self):
        testMessages = ('ыва завтра в 12:30', 
                        'ыва завтра в 12 часов lskdsdl jsalfsdk asdfkasdlkfj', 
                        '13.08.2022 в 12:30', 
                        '13 июля 2022 в 12:30 lskdsdl jsalfsdk asdfkasdlkfj alskd lkasdjfl sd12 22'
        )
        
        for msg in testMessages:
            self.setMessage(msg)
            print(self.getDate())
            print(self.getTime())
            print(self.MESSAGE)
            print('===============')


dp = DatetimeParser()
dp.test()

