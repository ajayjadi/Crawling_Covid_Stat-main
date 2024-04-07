# Crawling_Covid_Stat-main
Team Members 
Jadi Ajay (implemented module2 and module3.2- (1,2) )
Surajit Halder Kiran (implemented module1 and module 5)
Rohan Kadir Khan (implemented module 3.1, module 3.2-(3,4,5), module-4)


Execution for Module 3 and 4:
python3 run.py in Crawling_Covid_stat directory
run.py is a menu driven program that executes quries of modules 3.1 and 3.2.



to generate the links for timelines and responses
1. python3 T1_timeline.py
2. python3 T1_response.py

    there two files will generate 
        -> timeline_links.text
        -> response_links.txt
    
# now get data for the timelines
3. python3 get_data_timeline.py
    generates
    -> 2020
        -> Jan.txt
        -> feb.txt
        .
        .
        .
        .
        -> Dec.txt
    -> 2021
        same 
    -> 2022
        same
    -> 2023
        same
    -> 2024
        same

	#get data for responses
4. python3 get_data_responses.py
    -> response_2020
        -> Jan.txt
        -> feb.txt
        .
        .
        .
        .
        -> Dec.txt
    -> response_2021
        same
    -> response_2022
        same

### Extracting data for countries [india, australia, england, singapore, malaysia]

5. country_info.py
    -> prompts user to enter country name from above list
    -> it will get the corresponding page link from country_links.txt
    -> it will call get_data_by_country.py to get data for individual country and writes them in files
        -> malaysia_2020.txt
        -> malaysia_2021.txt
        -> malaysia_2022.txt
        -> malaysia_2023.txt
        -> malaysia_2024.txt
