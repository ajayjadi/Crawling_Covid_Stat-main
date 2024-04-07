import sys
from datetime import datetime

start_date_str = sys.argv[1]
end_date_str = sys.argv[2]

def is_date_in_range(start_date_str, end_date_str, check_date_str):
    start_date = datetime.strptime(start_date_str, "%d-%m-%Y")
    end_date = datetime.strptime(end_date_str, "%d-%m-%Y")
    check_date = datetime.strptime(check_date_str, "%d-%m-%Y")

    return start_date <= check_date <= end_date

for line in sys.stdin:
    line = line.strip()
    flag = 0
    date1 = line.strip("...").strip()
    if (line.startswith("...") and line.endswith("...") and "Background" not in line):
        if (is_date_in_range(start_date_str, end_date_str, date1)):
            print(line)
            flag = 1
            for inner_line in sys.stdin:
                inner_line = inner_line.strip()
                flag = 0
                date1 = inner_line.strip("...").strip()
                if (inner_line.startswith("...") and inner_line.endswith("...") and "Background" not in inner_line):
                    if (is_date_in_range(start_date_str, end_date_str, date1)):
                        print(inner_line)
                        continue
                    else:
                        break
                print(inner_line)
