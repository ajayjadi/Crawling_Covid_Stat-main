import sys
import os



data1=''
data2=''
country_name = sys.argv[1]
file_path = os.path.join(os.path.dirname(__file__), "..", "Module1", "all_info" + ".txt")
try:
    fp=open(file_path,'r')
    for line in fp:
        line=line.strip()
        line=line.split('\t')
        if line[0]== country_name:
            for i in line:
                i=i.strip()
                if i !=' ' and i !='\t':
                    data1+=i 
                    data1+='-'
            
        if line[0]== 'World':
            for i in line:
                i=i.strip()
                if i !=' ' and i!='\t':
                    data2+=i
                    data2+='-'
        
except FileNotFoundError:
        print(f"File '{file_path}' not found.")

print(data1[:-1])
print(data2[0:-1])