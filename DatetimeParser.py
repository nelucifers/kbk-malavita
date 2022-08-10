import datetime
import re

class DatetimeParser():

    def getDate(str):
        date = datetime.date.today()
        result = ''
        if str.find('послезавтра') >= 0:
            result = date + datetime.timedelta(days=2)
        elif str.find('завтра') >= 0:
            result = date + datetime.timedelta(days=1)
        elif str.find('сегодня') >= 0:
            result = date
        if result != False:
            pattern = r'(\d{1,2})\.?(\d{1,2})?\s?(янв|фев|мар|июн|июл|авг|сен|окт|ноя|дек)?'
            matches = re.search(pattern, str)
            result = matches.group(1) + '-'
        if matches.group(2):
            result += matches.group(2)
        return result

    def getTime(str):
        result = ''
        pattern = r'(\d{1,2})([:-](\d{1,2})|\s?ч[\.(ас)]?)'
        matches = re.search(pattern, str)
        result = matches.group(1) + '-'
        if matches.group(3):
            result += matches.group(3)
        else:
            result += '00'
        return result

str = 'ыва завтра в 12:30'
str = 'ыва завтра в 12 часов'
str = '13.08 в 12:30'
print(DatetimeParser.getDate(str))
print(DatetimeParser.getTime(str))