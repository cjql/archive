filename = '99csw.html'

with open(filename,'r',encoding='utf8') as f:
	rows = f.readlines()
    
rows.sort()

with open(filename,'w',encoding='utf8') as f:
	f.writelines(rows)