COVID-19 Data Extraction
This project consists of three Python scripts that extract and process COVID-19 data from the World Meters website.

Files
t1.py:
This script is responsible for downloading the web page from the World Meters website and parsing the data to generate the main.txt file.
The main.txt file contains the "Yesterday's Data" for the COVID-19 statistics.
t2.py:
This script is similar to t1.py, but it generates the main2.txt file, which contains the "Today's Data" for the COVID-19 statistics.
This project consists of three Python scripts that extract and process COVID-19 data from the World Meters website.

Files
t1.py:
This script is responsible for downloading the web page from the World Meters website and parsing the data to generate the main.txt file.
The main.txt file contains the "Yesterday's Data" for the COVID-19 statistics.
t2.py:
This script is similar to t1.py, but it generates the main2.txt file, which contains the "Today's Data" for the COVID-19 statistics.
t3.py:
This script combines the data from main.txt, main2.txt, and a newly generated main3.txt file to produce the final output in the extracted3_data.txt file.
The main3.txt file contains the "2 Day Ago Data" for the COVID-19 statistics.
The t3.py script uses the Lex and Yacc libraries for parsing the HTML content of the web page.
The extract_4_cases() function in t3.py extracts the "Active Cases", "Daily Deaths", "New Recovered", and "New Cases" for each country and writes them to the extracted3_data.txt file.
Workflow
The t1.py script downloads the web page from the World Meters website and generates the main.txt file.
The t2.py script downloads the web page from the World Meters website and generates the main2.txt file.
The t3.py script downloads the web page from the World Meters website and generates the main3.txt file.
The t3.py script then combines the data from main.txt, main2.txt, and main3.txt to produce the final output in the extracted3_data.txt file.
The extracted_data.txt file contains the COVID-19 statistics for each country, with the "Yesterday's Data", "Today's Data", and "2 Day Ago Data" displayed side-by-side.

Usage
To run the scripts, follow these steps:
Run main.py which sequentially executes t1,t2 and t3 and final output is saved in extracted_data.txt
Ensure you have the necessary dependencies installed, including ply (for Lex and Yacc) and urllib (for web page downloads).
OR Run the t1.py, t2.py, and t3.py scripts in sequence.
The final output will be generated in the extracted_data.txt file.