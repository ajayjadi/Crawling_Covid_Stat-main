import get_data_by_country 

fp = open("counrty_links.txt","r")
data  = fp.read()
data = data.strip()
data = data.split("\n")

dic = {}
for i in data:
    if(len(i)<10):
        if(dic.get(i) is None):
            dic[i] = []
        name = i
    else: 
        dic[name].append(i)

def get_data_by_countryname(cname):
    for item in dic[cname]:
        # print(item.split(" ")[1])
        get_data_by_country.main(item.split(" ")[0],cname+"_"+item.split(" ")[1])

while(True):
    print("enter country name (Australia, England, India, Malaysia,singapore) enter 1 to exit")
    cname = input()
    if(cname=="1"):
        exit()
    get_data_by_countryname(cname)
