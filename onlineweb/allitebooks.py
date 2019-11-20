import re
import requests


def get_book_urls(page):
    url = 'http://www.allitebooks.com/page/{}/'.format(page)
    res = requests.get(url).text
    urls = re.findall(r'"entry-title"><a href="(.*?)" rel="bookmark">(.*?)</a>',res)
    return(urls)

for page in range(1,809):
    url = 'http://www.allitebooks.com/page/{}/'.format(page)
    res = requests.get(url).text
    urls = re.findall(r'"entry-title"><a href="(.*?)" rel="bookmark">(.*?)</a>',res)
    # print(len(urls))
    print(page)
    for url in urls:
        title = re.sub(r'[<>\\\/|:?*"]','_',url[1])
        with open('{}_{}.md'.format(809-page,title),'w',encoding='utf8') as f:
            f.write(url[0])  
            print(url[1])
