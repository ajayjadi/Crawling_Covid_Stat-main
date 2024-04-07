import os
import ply.lex as lex
import ply.yacc as yacc
from urllib.request import Request, urlopen
req = Request('https://en.wikipedia.org/wiki/Responses_to_the_COVID-19_pandemic_in_March_2020',headers ={'User-Agent':'Mozilla/5.0'})
webpage = urlopen(req).read()
mydata = webpage.decode("utf8")
f=open('webpage.html','w',encoding="utf-8")
f.write(mydata)
f.close
