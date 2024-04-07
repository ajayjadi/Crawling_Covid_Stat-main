import os
import re
import sys

def filter_files_by_country(country_name_inp, directory_inp):
    relevant_files = [filename for filename in os.listdir(directory_inp) if country_name_inp.lower() in filename.lower()]
    return relevant_files

def extract_year_from_filename(filename_inp):
    match = re.search(r'\d{4}', filename_inp)
    if match:
        return match.group(0)
    else:
        return None

def merge_files_into_one(output_filename_inp, file_list_inp, directory_inp):
    with open(output_filename_inp, 'w') as outfile:
        for filename in file_list_inp:
            country_year = extract_year_from_filename(filename)
            if country_year is None:
                print(f"Failed to extract year from filename: {filename}")
                continue
            with open(os.path.join(directory_inp, filename), 'r') as infile:
                skip_line = False
                for line in infile:
                    if "Notes" in line or "References" in line or "see also" in line:
                        skip_line = True
                        continue
                    if skip_line:
                        skip_line = False
                        continue
                    date_format = re.search(r'(\d{1,2} [a-zA-Z]+)', line)
                    if date_format:
                        date_format = date_format.group(1)
                        formatted_date = f'{date_format}-{country_year}'
                        line = line.replace(date_format, formatted_date)
                    elif line.strip().split(" ")[0].strip() in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']:
                        month_format = line.strip().split(" ")[0].strip()
                        formatted_date = f'01-{month_format}-{country_year}'
                        line = f"{formatted_date} {line[len(month_format):]}"
                    else:
                        month_format = re.search(r'(?<=\W)\w{3,}(?=\W|$)', line)
                        if month_format:
                            month_format = month_format.group(0)
                            formatted_date = f'01-{month_format}-{country_year}'
                            line = re.sub(r'(?<=\W)\w{3,}(?=\W|$)', formatted_date, line)
                    outfile.write(line)


def extract_dates_and_content_from_file(filename_inp):
    dates = []
    content = []
    with open(filename_inp, 'r') as file:
        current_date = None
        for line in file:
            if len(line.strip()) < 45 and len(line.strip()) >10 and (line.strip().replace(".",""))[0].isdigit() and "Timeline" not in line:
                current_date = line.strip().replace(".","")
                current_date = current_date.replace(" ","-")
                if current_date[3].isdigit():
                    current_date=current_date[3:]
                if current_date[2].isdigit():
                    current_date=current_date[2:]
                if current_date[3]=='S':
                    current_date=None
            else:
                if current_date:
                    dates.append(current_date)
                    content.append(line.strip())
                    current_date = None
    return dates, content


mydict={'January':'01','February':'02','March':'03','April':'04','May':'05','June':'06','July':'07','August':'08','September':'09','October':'10','November':'11','December':'12'}

def main():
    country_name_inp = sys.argv[1]
    parent_directory_inp = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    directory_inp = os.path.join(parent_directory_inp, "Module2")
    relevant_files_inp = filter_files_by_country(country_name_inp, directory_inp)
    if not relevant_files_inp:
        print("No files found for the given country.")
        return

    output_filename_inp = os.path.join(os.getcwd(), f"{country_name_inp.lower()}_data.txt")
    merge_files_into_one(output_filename_inp, relevant_files_inp, directory_inp)

    dates, content = extract_dates_and_content_from_file(output_filename_inp)

    for i, info in zip(dates, content):
        date=i.split('-')
        if len(date)>=3:
            if date[0]=='0':
                date[0]=1
            print(f"{date[0]}-{mydict[date[1]]}-{date[2]}")
            

if __name__ == "__main__":
    main()
