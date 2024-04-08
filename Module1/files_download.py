import os
from urllib.request import urlopen, Request
from urllib.error import URLError

# Function to create directory if it doesn't exist
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Function to save HTML content to file
def save_html(url, filename):
    response = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        webpage = urlopen(response).read()
        mydata = webpage.decode("utf8")
        with open(filename, 'w', encoding="utf-8") as f:
            f.write(mydata)
        print(f"Successfully saved: {filename}")
    except URLError as e:
        print(f"Failed to fetch data from {url}: {e}")

def compile_country_list():
    filename = "worldometers_countrylist.txt"
    with open(filename) as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    region = ""
    is_sublist = 0
    region_country_map = {}

    for line in lines:
        if line.endswith(":"):
            line = line.strip(':')
            region = line
            region_country_map[region] = []
        elif not line:
            is_sublist = 1
        elif line.endswith("-"):
            is_sublist = 0
        elif is_sublist == 1:
            line = line.strip()
            region = line
            region_country_map[region] = []
        else:
            line = line.strip()
            region_country_map[region].append(line)

    return region_country_map

# Main URL
main_url = "https://www.worldometers.info/coronavirus/"

# Save main URL HTML
save_html(main_url, "main_page.html")

# Compile country list
country_map = compile_country_list()

# Iterate through continents and countries to save HTML files
for continent, countries in country_map.items():
    continent_directory = os.path.join("continents", continent)
    create_directory(continent_directory)
    
    for country in countries:
        country_url = f"{main_url}/country/{country.replace(' ', '-').lower()}/"
        filename = os.path.join(continent_directory, f"{country}.html")
        save_html(country_url, filename)
