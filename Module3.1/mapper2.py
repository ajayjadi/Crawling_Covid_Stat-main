import sys
import os
from datetime import datetime

def analyze_country_info(country_name, start_date, end_date):
    file_path = os.path.join(os.path.dirname(__file__), "..", "Module1", "country_info", country_name, country_name + ".txt")
    try:
        with open(file_path, 'r') as file:

            start=[]
            end=[]
            # Skip the header line
            next(file)
            # Read the lines in the file
            lines = file.readlines()
            # Find and print data for start_date
            start_date_found = False
            for line in lines:
                parts = line.strip().split('\t')
                if parts[0] == start_date:
                    for i in range(4):
                        if parts[i+1]=='NA':
                            start.append(0)
                        else:
                            start.append(int(parts[i+1]))
                    #print("\t".join(parts))
                    start_date_found = True
                    break  # Stop searching after finding start_date
            if not start_date_found:
                print(f"No data found for start date: {start_date}")
            
            # Find and print data for end_date
            end_date_found = False
            for line in lines:
                parts = line.strip().split('\t')
                if parts[0] == end_date:
                    for i in range(4):
                        if parts[i+1]=='NA':
                            end.append(0)
                        else:
                            end.append(int(parts[i+1]))
                    #print("\t".join(parts))
                    end_date_found = True
                    break  # Stop searching after finding end_date
            if not end_date_found:
                print(f"No data found for end date: {end_date}")
            
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    #print(start,end)
    print(country_name,'$',end='')
    for i in range(len(start)):
        if start[i]==0:
            print(end[i],'$',end='')
        else:
            print(abs((end[i]-start[i])/start[i]),'$',end='')
    print('\n')

country_name = sys.argv[1]
start_date = datetime.strptime(sys.argv[2], "%d-%m-%Y").strftime("%b %d, %Y")
end_date = datetime.strptime(sys.argv[3], "%d-%m-%Y").strftime("%b %d, %Y")

analyze_country_info(country_name, start_date, end_date)
country_list=['France','UK','Russia','Italy','Germany','Spain','Poland','Netherlands','Ukraine','Belgium','USA','Mexico','Canada','Cuba','Costa Rica','Panama','India','Turkey','Iran','Indonesia','Philippines','Japan','Israel','Malaysia','Thailand','Vietnam','Iraq','Bangladesh','Pakistan','Brazil','Argentina','Colombia','Peru','Chile','Bolivia','Uruguay','Paraguay','Venezuela','South Africa','Morocco','Tunisia','Ethiopia','Libya','Egypt','Kenya','Zambia','Algeria','Botswana','Nigeria','Zimbabwe','Australia','Fiji','Papua New Guinea','New Caledonia','New Zealand']
for country in country_list:
    if country != country_name:
        analyze_country_info(country, start_date, end_date)
