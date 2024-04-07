import sys
from datetime import datetime

datelist=[]
for line in sys.stdin:
    line=line.strip()
    #print(line)
    datelist.append(line)

# Parse dates into datetime objects
parsed_dates = [datetime.strptime(date_str, "%d-%m-%Y") for date_str in datelist]


# Find smallest and highest dates
smallest_date = min(parsed_dates)
highest_date = max(parsed_dates)

print('DateRange:')
print(smallest_date.strftime("%d-%m-%Y"),end=' to ')
print(highest_date.strftime("%d-%m-%Y"))
