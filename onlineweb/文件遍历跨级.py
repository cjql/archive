import os
dir = os.getcwd() 
dires = [] 
for root,dirs,files in os.walk(dir):  
    for file in files:  
        form = "<a href='{}'>{}</a><br>\n".format(os.path.join(root,file).replace(dir,'.'),file)
        dires.append(form)
        

with open("zdw.html",'w',encoding='utf8') as f:
    f.writelines(dires)