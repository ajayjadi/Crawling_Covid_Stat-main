import ply.lex as lex
import ply.yacc as yacc
from urllib.request import Request, urlopen  

### DEFINING TOKENS ###
tokens = ('BEGIN_MARK', 'END_MARK', 'OPEN_TAG', 'CLOSE_TAG', 'OPEN_LINK', 'CLOSE_LINK', 'TEXT', 'IGNORE')

t_ignore = ' \t\n'
# List to store all the values
data_list = []
file_path = "timeline_links.txt"

############### Tokenizer Rules ################
def t_BEGIN_MARK(t):
    r'<span.class="mw-headline".id="Worldwide_timelines_by_month_and_year">Worldwide.timelines.by.month.and.year'
    return t

def t_END_MARK(t):
    r'<dt>Responses</dt>'
    return t

def t_OPEN_TAG(t):
    r'<li[^>]*>'
    return t
 
def t_CLOSE_TAG(t):
    r'</li>'
    return t

def t_OPEN_LINK(t):
    r'<a[^>]*>'
    return t
 
def t_CLOSE_LINK(t):
    r'</a>'
    return t

def t_IGNORE(t):
    r"(<[^>]*> | &nbsp; | &\#160;)"
    t.lexer.skip(0)

def t_TEXT(t):
    r'[A-Za-z0-9 \.\–\/]+'
    return t

def t_error(t):
    t.lexer.skip(1)

####################################################################################################################################################################################################
# Grammar Rules
def p_start(p):
    '''start : table'''
    p[0] = p[1]

def p_skiptag(p):
    '''skiptag : content skiptag
               | IGNORE skiptag
               | OPEN_TAG skiptag
               | CLOSE_TAG skiptag
               | OPEN_LINK skiptag
               | CLOSE_LINK skiptag
               | empty 
      '''

def p_handlelink(p):
    '''handlelink : OPEN_LINK content CLOSE_LINK handlelink
                  |

    '''
    if len(p) > 1:
        p[0] = p[1]

def p_skiplink(p):
    '''skiplink : OPEN_LINK content CLOSE_LINK skiplink
                | content skiplink
                |
    '''
    pass

def p_handlelist(p):
    '''handlelist : OPEN_TAG handlelink CLOSE_TAG handlelist
                  | OPEN_TAG handlelist CLOSE_TAG handlelist
                  | OPEN_TAG content handlelist CLOSE_TAG handlelist
                  | content handlelist
                  |
    '''
    if len(p) == 5:
        with open(file_path, "a") as f:
            f.write(str(p[2]) + "\n")

def p_table(p):
    '''table : skiptag BEGIN_MARK skiplink handlelist END_MARK skiptag '''

def p_empty(p):
    '''empty :'''
    pass
 
def p_content(p):
    '''content : TEXT content
               | empty'''
    if len(p) == 3:
        p[0] = str(p[1]) + str(p[2])
    else:
        p[0] = ""
 
def p_error(p):
    pass

def main():
    link = f"https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic"
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    mydata = webpage.decode("utf8")
    with open('webpage.html', 'w', encoding="utf-8") as f:
        f.write(mydata)

    print("Fetching data.... Please wait....")
    with open('webpage.html', 'r', encoding="utf-8") as file_obj:
        data = file_obj.read()
        lexer = lex.lex()
        lexer.input(data)
        for tok in lexer:
            pass
        parser = yacc.yacc()
        parser.parse(data)

if __name__ == '__main__':
    main()
