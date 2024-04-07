import sys
from datetime import datetime

start=sys.argv[1]
end=sys.argv[2]
start_date = datetime.strptime(start, "%d-%m-%Y")
end_date = datetime.strptime(end, "%d-%m-%Y")

for line in sys.stdin:
    line=line.strip()
    line=line.split(':')

    date=datetime.strptime(line[0], "%d-%m-%Y")
    if start_date <= date <= end_date:
        print(line[0])
        print(line[1])
