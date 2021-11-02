"""
import datetime
today = datetime.date.today();
print('today is ', today)
"""

from datetime import date
today = date.today();
print('today is ', today)
print(today.year, '년도')





from datetime import date
from datetime import timedelta
today = date.today();

print( '어제', today + timedelta(days=-1))
print( '일주일후', today + timedelta(weeks=1))
print( '10일전', today + timedelta(days=-10))