import os

import ply.lex as lex
import ply.yacc as yacc

import re

a = []
###DEFINING TOKENS###
tokens = ('BEGINTABLE', 'CAPTIONOPEN','CAPTIONCLOSE','OPENBODY','CLOSEBODY',
'OPENTABLE', 'CLOSETABLE', 'OPENROW', 'CLOSEROW','TABLENAME', 'OPENI','CLOSEI',
'OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF',
'CONTENT', 'OPENDATA', 'CLOSEDATA' ,'OPENSPAN',
'CLOSESPAN', 'OPENDIV', 'CLOSEDIV', 'OPENSTYLE', 'CLOSESTYLE','GARBAGE','POPEN','PCLOSE','ULOPEN','ULCLOSE','LOPEN','LCLOSE','H2OPEN','H2CLOSE','H3OPEN','H3CLOSE','CONTENT1','LINKOPEN','END')

t_ignore= ' '

###############Tokenizer Rules################
def t_TABLENAME(t):
     r'<meta.property="mw:PageProp/toc"./>'
     return t

def t_END(t):
     r'<span.class="mw-headline".id="See_also">See.also'
     return t
def t_H2OPEN(t):
    r'<h2[^>]*>'
    return t

def t_H2CLOSE(t):
    r'</h2[^>]*>'
    return t


def t_H3OPEN(t):
    r'<h3[^>]*>'
    return t

def t_H3CLOSE(t):
    r'</h3[^>]*>'
    return t


def t_POPEN(t):
    r'<p[^>]*>'
    return t

def t_PCLOSE(t):
    r'</p[^>]*>'
    return t


def t_ULOPEN(t):
    r'<ul[^>]*>'
    return t

def t_ULCLOSE(t):
    r'</ul[^>]*>'
    return t

def t_LINKOPEN(t):
    r'<link[^>]*>'
    return t

def t_LOPEN(t):
    r'<li[^>]*>'
    return t

def t_LCLOSE(t):
    r'</li[^>]*>'
    return t



def t_OPENTABLE(t):
    r'<table[^>]*>'
    return t

def t_CLOSETABLE(t):
    r'</table[^>]*>'
    return t

def t_CAPTIONOPEN(t):
    r'<caption[^>]*>'
    return t

def t_CAPTIONCLOSE(t):
    r'</caption[^>]*>'
    return t



def t_OPENBODY(t):
    r'<tbody[^>]*>'
    return t

def t_CLOSEBODY(t):
    r'</tbody[^>]*>'
    return t

def t_OPENROW(t):
    r'<tr[^>]*>'
    return t

def t_CLOSEROW(t):
    r'</tr[^>]*>'
    return t

def t_OPENHEADER(t):
    r'<h4[^>]*>'
    return t

def t_CLOSEHEADER(t):
    r'</h4[^>]*>'
    return t

def t_OPENHREF(t):
    r'<a[^>]*>'
    

def t_CLOSEHREF(t):
    r'</a[^>]*>'
    

def t_OPENDATA(t):
    r'<td[^>]*>'
    return t

def t_CLOSEDATA(t):
    r'</td[^>]*>'
    return t


def t_OPENI(t):
    r'<i>'
    

def t_CLOSEI(t):
    r'</i>'
    



def t_CONTENT(t):
    r'\#8211|\#160|\#58|\#BeActive|[A-Za-z0-9:,/(). ]+'
    return t

def t_CONTENT1(t):
    r'[#0-9]+'
    return t

def t_OPENDIV(t):
    r'<div[^>]*>'
    return t

def t_CLOSEDIV(t):
    r'</div[^>]*>'
    return t

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
    return t


def t_error(t):
    t.lexer.skip(1)

def p_start(p):
    '''start : table'''





def p_table(p):
    '''table :   TABLENAME  heading  
                 '''
    #print(p[1])

def p_handlecontent(p):
    '''handlecontent : H2OPEN CONTENT  CONTENT  H2CLOSE

    '''
    with open("Response_March_2020.txt", "a") as file:
        file.write("\n" + p[2] + '\n' )
        print()
        print()
        print(p[2])

def p_heading(p):
    ''' heading : handlecontent date heading
                    | handlecontent POPEN content PCLOSE date heading
                    | empty  '''
    if (len(p) == 7):
        #print(p[2]) 
        a.append(p[2])


def p_handledate(p):
    '''handledate : H3OPEN CONTENT  CONTENT  H3CLOSE

    '''
    with open("Response_March_2020.txt", "a") as file:
        file.write("\n" + p[2]+ "\n")
    print()
    print(p[2])

def p_date(p):
    ''' date : handledate data date
                | skiptag2 date
                | empty'''
    if (len(p) == 7):
        #`print(p[2]) 
        a.append(p[2])


def p_data(p):
    ''' data : ULOPEN   line  ULCLOSE data
                | POPEN content PCLOSE data
                | skiptag content data
                | skiptag2 data
                
                | empty'''


def p_line(p):
    ''' line :  LOPEN  content LCLOSE line
                | empty'''

li = []
def p_printcontent(p):
    ''' printcontent : CONTENT

    '''
    
    #print(p[1])
    with open("Response_March_2020.txt", "a") as file:
        file.write(p[1]+ " ")
    print(p[1],end = " ")

def p_content(p):
    ''' content : printcontent skiptag content

                
                | empty '''

   
    

    


def p_skiptag(p):
    ''' skiptag : GARBAGE skiptag
                | CONTENT1 CONTENT CONTENT1 skiptag
                | CONTENT1 CONTENT CONTENT CONTENT1 skiptag
                | OPENHREF skiptag
                | CLOSEHREF skiptag
                | OPENI skiptag
                | CLOSEI skiptag
                
                | empty '''

def p_skiptag2(p):
    ''' skiptag2 : OPENSTYLE skiptag2 CLOSESTYLE skiptag2 
                | CONTENT skiptag2

                | OPENSTYLE skiptag2
                | CLOSESTYLE skiptag2
                | OPENBODY  skiptag2
                | OPENROW skiptag2
                | OPENDATA skiptag2
                | OPENI skiptag2
                | OPENDIV skiptag2
                | OPENTABLE skiptag2
                | CLOSEBODY  skiptag2
                | CLOSEROW skiptag2
                | CLOSEDATA skiptag2
                | CLOSEI skiptag2
                | CLOSEDIV skiptag2
                | CLOSETABLE skiptag2
                | GARBAGE skiptag2
                | CONTENT1 skiptag2
                | LINKOPEN skiptag2
                | empty '''



def p_empty(p):
    '''empty :'''

  


def p_error(p):
    #print("error")
    pass




file_obj= open('webpage.html','r',encoding="utf-8")
data=file_obj.read()
lexer = lex.lex()
lexer.input(data)
for tok in lexer:
    print(tok)
parser = yacc.yacc()
parser.parse(data)
#for i in range(len(a)-1,0,-1):
#    print(a[i],end=' ')

file_obj.close()

