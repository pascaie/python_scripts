# inputs:
# total cost of the bill
# month of the year
# number of Rosario's days abroad

import sys
import calendar
from datetime import date as dt

supportEmail = 'enrico.pascai@gmail.com'
thisMonth = dt.today().month

selectMonth = input('Is the bill relative to the current month ('
                + calendar.month_name[thisMonth]
                + ')? [y/n] ')

if selectMonth in ('n', 'N', 'no', 'NO'):
    selectMonth = input('Is the bill relative to the previous month ('
                    + calendar.month_name[thisMonth - 1]
                    + ')? [y/n] ')
    if selectMonth in ('n', 'N', 'no', 'NO'):
        print('Sorry, this script was not thought to take into account bills dated earlier than two monts from your current date')
        print('For this purpose, we may have to set up a cluster to handle the increased computational effort, with the related additional costs for the end user')
        print('Please, contact the support team by email (' + supportEmail + ') or wait for release 2.0')
        sys.exit()
    else:
        monthVar = thisMonth - 1
else:
    monthVar = thisMonth

print(monthVar)

print(calendar.monthrange(2018, 11)[1])
