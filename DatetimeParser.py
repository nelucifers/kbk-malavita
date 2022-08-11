import datetime
from dateutil import parser as dp
import re


class parser():

    _message = ''

    def setMessage(self, message):
        self._message = message


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
        message = self._message

        date = datetime.date.today()
        result = ''
        if self._message.find('послезавтра') >= 0:
            result = date + datetime.timedelta(days=2)
        elif self._message.find('завтра') >= 0:
            result = date + datetime.timedelta(days=1)
        elif self._message.find('сегодня') >= 0:
            result = date

        if result == '':
            year = str(date.year)
            month = ''
            pattern = r'^(\d{1,2})\.?(\d{1,2})?\s?((янв|фев|мар|июн|июл|авг|сен|окт|ноя|дек).+?)?\s?\.?(\d{4})?'
            matches = re.search(pattern, self._message)
            self._message = re.sub(pattern, '', self._message).strip()
            print('message=', self._message)
            # print(matches)
            if(matches != None):
                day = matches.group(1)
                # length = len(matches.group(0))
                # message = message[length:]
                # print(message)
                if int(day) < 10:
                    day = '0' + day
                if matches.group(2):
                    month = matches.group(2)
                elif(matches.group(4)):
                    month = self.monthToNum(matches.group(4))
                    # if month.isdigit():
                    #     result += month + '.'
                    # else:
                    #     monthNumber = self.monthToNum(month)
                    #     # print(monthNumber)
                    #     result += str(monthNumber) + '.'
                if matches.group(5):
                    year = matches.group(5)
                result = year + '-' + month + '-' + day

        return str(result)


    def getTime(self):
        message = self._message

        result = ''
        pattern = r'(\d{1,2})([:-](\d{1,2})|\s?ч(\.|(ас\w+))?)'
        matches = re.search(pattern, self._message)

        if(matches != None):
            length = matches.span(0)[0]
            self._message = self._message[length:].strip()
            print(self._message)
            self._message = re.sub(pattern, '', self._message).strip()
            print('message=', self._message)
            print(matches)
            # message = message.replace(matches.group(0), '')
            result = matches.group(1) + ':'
            if matches.group(3):
                result += matches.group(3)
            else:
                result += '00'
        
        return result
    
    def getDateTime(self):
        date = self.getDate()
        time = self.getTime()
        datetime = date + " " + time
        return dp.parse(datetime)

