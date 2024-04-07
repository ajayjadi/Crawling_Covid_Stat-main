import ply.lex as lex
import ply.yacc as yacc
from urllib.request import Request, urlopen
import numpy as np

global_country_data, all_country_data, country_data_dict = [], [], {}

t_ignore='        \t\n'
###DEFINING TOKENS###
tokens = ('BEGINTABLE',
'OPENTABLE', 'OPENHEAD','CLOSEHEAD','CLOSETABLE', 'OPENROW', 'CLOSEROW',
'OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF','WASTE',
'CONTENT', 'OPENDATA', 'CLOSEDATA' ,'OPENSPAN',
'CLOSESPAN', 'OPENDIV', 'CLOSEDIV', 'OPENSTYLE', 'CLOSESTYLE','GARBAGE')

###############Tokenizer Rules################
                                
def t_BEGINTABLE(t):
    r'<table.id="main_table_countries_yesterday2".class="table.table-bordered.table-hover.main_table_countries".style="width:100%;margin-top:.0px.!important;display:none;">'
    return t

def t_OPENTABLE(t):
    r'<tbody[^>]*>'
    return t

def t_CLOSETABLE(t):
    r'</tbody[^>]*>'
    return t

def t_OPENHEAD(t):
    r'<thead[^>]*>'
    return t

def t_CLOSEHEAD(t):
    r'<\thead[^>]*>'
    return t

def t_OPENROW(t):
    r'<tr[^>]*>'
    return t

def t_CLOSEROW(t):
    r'</tr[^>]*>'
    return t

def t_OPENHEADER(t):
    r'<th[^>]*>'
    return t

def t_CLOSEHEADER(t):
    r'</th[^>]*>'
    return t

def t_OPENHREF(t):
    r'<a[^>]*>'
    return t

def t_CLOSEHREF(t):
    r'</a[^>]*>'
    return t

def t_OPENDATA(t):
    r'<td[^>]*>'
    return t

def t_CLOSEDATA(t):
    r'</td[^>]*>'
    return t

def t_WASTE(t):
    r'&\#160;'
    return t

def t_CONTENT(t):
    r'[A-Za-z0-9+,.\/\u00E9 ]+'
    return t

def t_OPENDIV(t):
    r'<div[^>]*>'

def t_CLOSEDIV(t):
    r'</div[^>]*>'

def t_OPENSTYLE(t):
    r'<style[^>]*>'
    return t

def t_CLOSESTYLE(t):
    r'</style[^>]*>'
    return t

def t_OPENSPAN(t):
    r'<span[^>]*>'

def t_CLOSESPAN(t):
    r'</span[^>]*>'

def t_GARBAGE(t):
    r'<[^>]*>'

def t_error(t):
    t.lexer.skip(1)

####################################################################################################################################################################################################
											#GRAMMAR RULES
    


def p_start(p):
    '''start : table'''
    p[0] = p[1]



def p_skiptag1(p):
     '''skiptag1 : CONTENT skiptag1
               | OPENROW skiptag1
               | CLOSEROW skiptag1
               | OPENHEADER skiptag1
               | CLOSEHEADER skiptag1
               | OPENHEAD skiptag1
               | OPENTABLE
               | empty
               |
               '''
     
# def p_skiptag2(p):
#      '''skiptag2 : CONTENT skiptag2
#                | OPENDATA skiptag2
#                | CLOSEDATA skiptag2
#                | empty
#                 '''

def p_wasted(p):
    '''wasted : GARBAGE wasted
                | OPENHREF wasted
                | CLOSEHREF wasted
                | CONTENT wasted
                | OPENDATA wasted
                | CLOSEDATA wasted
                | OPENSPAN wasted
                | CLOSESPAN wasted
                | OPENHEADER wasted
                | WASTE wasted
                | CLOSEHEADER wasted
                | empty'''

def p_skip_row(p):
     '''skip_row :  OPENROW wasted CLOSEROW'''





# # # def p_handleheader(p):
# # #     '''handleheader : OPENHEADER CONTENT CLOSEHEADER dataCell
# # #                     | OPENHEADER skiptag CLOSEHEADER dataCell
# # #                     | OPENHEADER CONTENT CLOSEHEADER handleheader
# # #                     | empty'''


# # # def p_waste(p):

def p_dataCell(p):
    '''dataCell : OPENDATA CONTENT CLOSEDATA dataCell
                | OPENDATA OPENHREF content CLOSEHREF CLOSEDATA dataCell
                | OPENDATA CLOSEDATA dataCell
                | empty'''
    # if len(p) == 5 :
    #     print("Continous:",p[2])  
    # if len(p) == 7:
    #     print("Countries:",p[3])  
    global global_country_data
    if len(p) == 2:
        global all_country_data
        if len(global_country_data) != 0: all_country_data.append(global_country_data[:])
        global_country_data.clear()
    elif len(p) == 4: global_country_data.append(' ')
    elif len(p) == 5: global_country_data.append(p[2])
    else:
        ind1, ind2 = p[2].find('href="'), p[2].find('">')
        url = p[2][ind1+6:ind2]
        if url.find('country') != -1: global_country_data.append(url)
        global_country_data.append(p[3])

def p_skip_rows(p):
    '''skip_rows : skip_row skip_row skip_row skip_row skip_row skip_row skip_row'''



def p_handlerow(p):
    '''handlerow : OPENROW dataCell CLOSEROW handlerow
                 | empty'''
    

def p_table(p):
    '''table : BEGINTABLE skiptag1 skip_rows handlerow'''
    
def p_empty(p):
    '''empty :'''


def p_content(p):
    '''content : CONTENT content
               | empty'''
    if len(p)==3:
        p[0]=p[1]+p[2]
    else:
        p[0]=''

def p_error(p):
    pass


# Parse the given data
def parse_data(data):
    tokens_file = open('tokens.txt', 'w', encoding="utf-8")
    lexer = lex.lex()
    lexer.input(data)
    for tok in lexer:
        tokens_file.write(str(tok) + "\n")
    parser = yacc.yacc()
    parser.parse(data)

# Download the web page for the given URL and store it in the given file_name
def download_web_page(url, file_name):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    mydata = webpage.decode("utf8")
    with open(file_name, 'w', encoding="utf-8") as f:
        f.write(mydata)

# Extract data from the downloaded web page
def extract_data():
    file_obj = open('webpage.html', 'r', encoding="utf-8")
    data = file_obj.read()
    file_obj.close()
    parse_data(data)



    

# Extract the 4 cases (Active Cases, Daily Deaths, New Recovered, New Cases) for a given country
def extract_4_cases():
    # Open the three files
    with open('main.txt', 'r') as file1:
        data1 = file1.readlines()

    with open('main2.txt', 'r') as file2:
        data2 = file2.readlines()

    with open('main3.txt', 'r') as file3:
        data3 = file3.readlines()

# Create a new file to write the extracted data
    with open('extracted_data.txt', 'w') as output_file:
        output_file.write("Yesterday Data:\t\tToday's Data:\t\t2 Day Ago Data:\n\n")

    # Iterate through the files simultaneously
        for i in range(len(data1)):
            fields1 = data1[i].strip().split('\t')
            fields2 = data2[i].strip().split('\t')
            fields3 = data3[i].strip().split('\t')

            if len(fields1) == 12 and len(fields2) == 12 and len(fields3) == 12:
                country = fields1[0]
                active_cases1 = fields1[3]
                daily_deaths1 = fields1[9]
                new_recovered1 = fields1[11]
                new_cases1 = fields1[10]

                active_cases2 = fields2[3]
                daily_deaths2 = fields2[9]
                new_recovered2 = fields2[11]
                new_cases2 = fields2[10]

                active_cases3 = fields3[3]
                daily_deaths3 = fields3[9]
                new_recovered3 = fields3[11]
                new_cases3 = fields3[10]

                output_file.write(f"Country: {country}\n")
                output_file.write(f"Active Cases: {active_cases1}\t\tActive Cases: {active_cases2}\t\tActive Cases: {active_cases3}\n")
                
                if daily_deaths2 == fields1[9]:
                    output_file.write(f"Daily Deaths: {daily_deaths1}\t\tDaily Deaths: {daily_deaths2}\t\tDaily Deaths: {daily_deaths3}\n")
                else:
                    output_file.write(f"Daily Deaths: {daily_deaths1}\t\tDaily Deaths: +{daily_deaths2[1:]}\t\tDaily Deaths: +{daily_deaths3[1:]}\n")
                
                if new_recovered2 == fields1[11]:
                    output_file.write(f"New Recovered: {new_recovered1}\t\tNew Recovered: {new_recovered2}\t\tNew Recovered: {new_recovered3}\n")
                else:
                    output_file.write(f"New Recovered: {new_recovered1}\t\tNew Recovered: +{new_recovered2[1:]}\t\tNew Recovered: +{new_recovered3[1:]}\n")
                
                if new_cases2 == fields1[10]:
                    output_file.write(f"New Cases: {new_cases1}\t\tNew Cases: {new_cases2}\t\tNew Cases: {new_cases3}\n\n")
                else:
                    output_file.write(f"New Cases: {new_cases1}\t\tNew Cases: +{new_cases2[1:]}\t\tNew Cases: +{new_cases3[1:]}\n\n")





#########DRIVER FUNCTION#######
# Main function
def main():
    download_web_page('https://www.worldometers.info/coronavirus/', 'webpage.html')
    print("Started Extracting Data...")
    extract_data()


    # Processing extracted data
    countries = []
    with open('worldometers_countrylist.txt', 'r') as country_file:
        for line in country_file.readlines():
            countries.append(line.strip())

    
   
    with open('main3.txt', 'w') as file:
        arr = ['Country Name', 'Url', 'Total cases', 'Active Cases', 'Total Deaths', 
               'Total Recovered', 'Total Tests', 'Deaths/million', 'Tests/million', 
               'New Cases', 'New Death', 'New Recovery']
        ind = [1, 2, 3, 9, 5, 7, 13, 12, 14, 4, 6, 8]
        file.write('\t'.join(arr) + '\n')
        for i in all_country_data:
            i.reverse()
            for j in range(2, len(i)):
                i[j] = i[j].replace(',', '').replace(' ', '')
                if i[j] == '':
                    i[j] = '0'
            if i[1].lower() == 'world':
                country_data_dict[str(i[1]).lower()] = ['', 'world', ''] + i[2:]
                data = ['', 'world', ''] + i[2:]
            else:
                country_data_dict[str(i[1]).lower()] = i[:]
                data = i[:]
            if str(i[1]) in countries:
                val = [data[x] for x in ind]
                string = '\t'.join(val)
                file.write(string + '\n')

    # with open('data.txt', 'w') as file:
    #     for i in all_country_data:
    #         string = ','.join(i[0:14])
    #         file.write(string + '\n')

    # with open('global_countries_data.txt', 'w') as file:
    #     string = '\t'.join(arr)
    #     file.write(string + '\n')

    print("Data Extracted Successfully(	Final result is stored in extracted_data.txt)")

    extract_4_cases()

if __name__ == '__main__':
    main()
