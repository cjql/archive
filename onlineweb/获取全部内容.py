import os
path = os.getcwd()

a = []
for root,dirs,files in os.walk(path):  
    for file in files:
        filename = os.path.join(root,file)
        with open(filename,'r',encoding='utf8') as f:
            url = f.read()
            a.append(url)

with open('allitebooks.html','w',encoding='utf8') as f:
    f.writelines(a)
