with open('已购.txt','r',encoding='utf8') as f:
    lines = f.readlines()
    for line in lines:
        with open(line.strip(),'w',encoding='utf8') as f1:
            f1.write('')

    
    