import ply.lex as lex
import ply.yacc as yacc
from urllib.request import Request, urlopen  
import os
import get_data_2023
import get_data_2020




###DEFINING TOKENS###
tokens = ('BEGINTABLE', 'OPENPARA','CLOSEPARA','OPENHEAD','CLOSEHEAD',
'CONTENT','GARBAGE','ENDTABLE')

t_ignore = ' \t\n'
# lis to store all the values
lis = []


filep = open("2019.txt","w")
###############Tokenizer Rules################
def t_BEGINTABLE(t):
    r'<span.class="mw-headline".id="Unconfirmed_reports_of_early_cases">Unconfirmed.reports.of.early.cases</span>'
    return t

def t_ENDTABLE(t):
     r'<span.class="mw-headline".id="See_also">See.also'
     return t
def t_OPENPARA(t):
    r'<p[^>]*>'
    return t
 
def t_CLOSEPARA(t):
    r'</p>'
    return t

def t_OPENHEAD(t):
    r'<h2[^>]*>'
    return t
 
def t_CLOSEHEAD(t):
    r'</h2>'
    return t

def t_GARBAGE(t):
    r"(<[^>]*> | &nbsp; | &\#160;)"
    # print(t.value,len(t.value))
    t.lexer.skip(0)

def t_CONTENT(t):
    r'[A-Za-z0-9 \,\.\–\/]+'
    return t



def t_error(t):
    t.lexer.skip(1)
####################################################################################################################################################################################################
                                            #GRAMMAR RULES
def p_start(p):
    '''start : table'''
    p[0] = p[1]

def p_skiptag(p):
    '''skiptag : content skiptag
               | GARBAGE skiptag
               | OPENPARA skiptag
               | CLOSEPARA skiptag
               | OPENHEAD skiptag
               | CLOSEHEAD skiptag
               | empty 

      '''

def p_skiptag1(p):
    '''skiptag1 : content skiptag1
               | GARBAGE skiptag1
               | OPENPARA skiptag1
               | CLOSEPARA skiptag1
               
               | CLOSEHEAD skiptag1
               | empty 

      '''
def p_printpara(p):
    '''printpara : OPENPARA content CLOSEPARA'''
    # print(p[2])
    filep.write(f"{p[2]}\n")
    
def p_handlepara(p):
    '''handlepara :  printpara handlepara
                  
                  |

    '''
    if(len(p)==3):
        p[0]=p[1]

def p_printhead(p):
    '''printhead : OPENHEAD content CLOSEHEAD'''
    if(p[2]):
        # print(f"....{p[2]}....")
        filep.write(f"....{p[2]}....\n")

def p_handlehead(p):
    '''handlehead : printhead content printpara handlehead
                  | printpara handlehead
                  | content printpara handlehead
                  | OPENHEAD ENDTABLE skiptag
                  |
    '''
    if(len(p)== 6):
        # print(f"{p[4]}\n")
        filep.write(f"{p[4]}\n")
    elif(len(p)==4):
        # print(f"{p[2]}\n")
        filep.write(str(p[2])+"\n")
    # print(len(p))



def p_table(p):
    '''table : skiptag  BEGINTABLE skiptag1  handlehead '''

 
def p_empty(p):
    '''empty :'''
    pass
 
def p_content(p):
    '''content : CONTENT content
               | empty'''
    if(len(p)==3):
        if(p[1]!="edit"):
            
            
            p[0] = str(p[1])+str(p[2])
            
        
        else:
            p[0] = ""
        
    
 
def p_error(p):
    # print("\n\n\n\n\nerror....",p)
    pass
 
#########DRIVER FUNCTION#######
def fetch_webpage(link):
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    webpage_content = webpage.decode("utf8")
    with open('webpage.html', 'w', encoding="utf-8") as file:
        file.write(webpage_content)

    print("Fetching data.... Please wait....")
    with open('webpage.html', 'r', encoding="utf-8") as file_obj:
        data = file_obj.read()
        lexer = lex.lex()
        lexer.input(data)
        with open("lextokens.txt", "w") as fp:
            for tok in lexer:
                try:
                    fp.write(str(tok) + "\n")
                except:
                    pass
        parser = yacc.yacc()
        parser.parse(data)

if __name__ == '__main__':
    with open("timeline_links.txt", "r") as file:
        data = file.read()
        base = "https://en.wikipedia.org"
        for link in data.split("\n"):
            link = link.strip('">')
            attr = link.split(" ")
            if attr[-1] == "2019":
                print(base + attr[1].split("=")[1].strip('"'))
                fetch_webpage(base + attr[1].split("=")[1].strip('"'))
            elif attr[-1] in ["2020", "2021", "2022"]:
                get_data_2020.main(base + attr[1].split("=")[1].strip('"'), attr[-1], attr[-2])
            elif attr[-1] in ["2023", "2024"]:
                get_data_2023.main(base + attr[1].split("=")[1].strip('"'), attr[-1])




