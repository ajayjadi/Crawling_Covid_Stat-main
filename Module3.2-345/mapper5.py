import os
import re
import sys
from datetime import datetime

def filter_files_by_country(country_name, directory):
    relevant_files = [filename for filename in os.listdir(directory) if country_name.lower() in filename.lower()]
    return relevant_files

def extract_year_from_filename(filename):
    match = re.search(r'\d{4}', filename)
    if match:
        return match.group(0)
    else:
        # Handle the case where no year is found in the filename
        return None

def merge_files_into_one(output_filename, file_list, directory):
    with open(output_filename, 'w') as outfile:
        for filename in file_list:
            country_year = extract_year_from_filename(filename)
            if country_year is None:
                # Handle the case where year extraction fails
                print(f"Failed to extract year from filename: {filename}")
                continue
            with open(os.path.join(directory, filename), 'r') as infile:
                skip_line = False
                for line in infile:
                    if "Notes" in line or "References" in line or "see also" in line:
                        skip_line = True
                        continue
                    if skip_line:
                        skip_line = False
                        continue
                    date_format = re.search(r'(\d{1,2} [a-zA-Z]+)', line)  # Check for lines containing date or date month
                    if date_format:
                        date_format = date_format.group(1)
                        formatted_date = f'{date_format}-{country_year}'
                        line = line.replace(date_format, formatted_date)
                    elif line.strip().split(" ")[0].strip() in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']:
                        month_format = line.strip().split(" ")[0].strip()
                        formatted_date = f'01-{month_format}-{country_year}'
                        line = f"{formatted_date} {line[len(month_format):]}"  # Append the formatted date at the beginning of the line
                    else:
                        month_format = re.search(r'(?<=\W)\w{3,}(?=\W|$)', line)
                        if month_format:
                            month_format = month_format.group(0)
                            formatted_date = f'01-{month_format}-{country_year}'
                            line = re.sub(r'(?<=\W)\w{3,}(?=\W|$)', formatted_date, line)
                    outfile.write(line)


def extract_dates_and_content_from_file(filename):
    dates = []
    content = []
    with open(filename, 'r') as file:
        current_date = None
        for line in file:
            # Check if line is a date line
            if len(line.strip()) < 45 and len(line.strip()) >10 and (line.strip().replace(".",""))[0].isdigit() and "Timeline" not in line:
                # Extract the date
                current_date = line.strip().replace(".","")
                current_date = current_date.replace(" ","-")
                if current_date[3].isdigit():
                    current_date=current_date[3:]
                if current_date[2].isdigit():
                    current_date=current_date[2:]
                if current_date[3]=='S':
                    current_date=None
            else:
                # Add the date and content to their respective lists
                if current_date:
                    dates.append(current_date)
                    content.append(line.strip())
                    current_date = None
    return dates, content


mydict={'January':'01','February':'02','March':'03','April':'04','May':'05','June':'06','July':'07','August':'08','September':'09','October':'10','November':'11','December':'12'}
countrylist=['australia','england','india','malaysia','singapore']

def main():
    start=sys.argv[1]
    end=sys.argv[2]
    start_date = datetime.strptime(start, "%d-%m-%Y")
    end_date = datetime.strptime(end, "%d-%m-%Y")
    parent_directory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))  # Get parent directory
    directory = os.path.join(parent_directory, "Module2")
    data=''
    for j in countrylist:
        relevant_files = filter_files_by_country(j, directory)
        if not relevant_files:
            print("No files found for the given country.")
            return

        output_filename = os.path.join(os.getcwd(), f"{j.lower()}_data.txt")
        merge_files_into_one(output_filename, relevant_files, directory)

        dates, content = extract_dates_and_content_from_file(output_filename)
        
        for i, info in zip(dates, content):
            date=i.split('-')
            if len(date)>=3:
                if date[0]=='0':
                    date[0]=1
                datevalue=f"{date[0]}-{mydict[date[1]]}-{date[2]}"
                dateval=datetime.strptime(datevalue, "%d-%m-%Y")
                if start_date <= dateval <= end_date:
                    data+=f"{j}:{datevalue}:{info}\n"
            
    print(data[:-1])
if __name__ == "__main__":
    main()
