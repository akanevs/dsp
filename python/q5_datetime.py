# Hint:  use Google to find python function
'''
####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

####b)  
date_start = '12312013'  
date_stop = '05282015'  

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  
'''

import time
from datetime import date

#print(date_start)
#today = date.today()
#today
#datetime.date(2007, 12, 5)

date_start = '01-02-2013'    
date_stop = '07-28-2015'

m1 = date_start[0:2]
d1 = date_start[3:5]
y1 = date_start[6:10]

m2 = date_stop[0:2]
d2 = date_stop[3:5]
y2 = date_stop[6:10]

date_1 = date(int(y1), int(m1), int(d1))
date_2 = date(int(y2), int(m2), int(d2))

diff = abs(date_1-date_2).days
print(diff,'days')

#===============================

date_start = '12312013'  
date_stop = '05282015'  

m1 = date_start[0:2]
d1 = date_start[2:4]
y1 = date_start[4:8]

m2 = date_stop[0:2]
d2 = date_stop[2:4]
y2 = date_stop[4:8]

date_1 = date(int(y1), int(m1), int(d1))
date_2 = date(int(y2), int(m2), int(d2))

diff = abs(date_1-date_2).days
print(diff,'days')

#===============================

import calendar

date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  

m1 = date_start[3:6]
d1 = date_start[0:2]
y1 = date_start[7:11]

m2 = date_stop[3:6]
d2 = date_stop[0:2]
y2 = date_stop[7:11]

abbr_to_num = {name: num for num, name in enumerate(calendar.month_abbr) if num}
#>>> abbr_to_num['Jan']

#find integer for given 3-letter month name 
m1 = abbr_to_num[m1]
m2 = abbr_to_num[m2]

date_1 = date(int(y1), int(m1), int(d1))
date_2 = date(int(y2), int(m2), int(d2))

diff = abs(date_1-date_2).days
print(diff,'days')

