import sys

file_name = sys.argv[1]

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

try:
    with open(file_name, 'r') as file:
        data = file.read()
        data = data.split("\n")
        
        for line in data:
            line = line.strip()
            
            if 0 < len(line) < 30:
                line = line.strip("...")
                if " " in line and line.split(" ")[1] in months:
                    month = str(months.index(line.split(" ")[1]) + 1).rjust(2, "0")
                    day = str(line.split(" ")[0]).rjust(2, "0")
                    print("..." + day + "-" + month + "-" + str(file_name.split("/")[3]) + "...")
            else:
                print(line)

except IOError as e:
    pass
