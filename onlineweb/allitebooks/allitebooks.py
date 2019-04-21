import re
import requests


def get_book_urls(page):
    url = 'http://www.allitebooks.com/page/{}/'.format(page)
    res = requests.get(url).text
    urls = re.findall(r'"entry-title"><a href="(.*?)" rel="bookmark">(.*?)</a>',res)
    return(urls)

for page in range(478,809):
    url = 'http://www.allitebooks.com/page/{}/'.format(page)
    res = requests.get(url).text
    urls = re.findall(r'"entry-title"><a href="(.*?)" rel="bookmark">(.*?)</a>',res)
    # print(len(urls))
    print(page)
    for url in urls:
        title = re.sub(r'[<>\\\/|:?*"]','_',url[1])
        with open('{}.md'.format(title),'w',encoding='utf8') as f:
            f.write(url[0])  
            print(url[1])
    # print(urls[0],urls[1])
    # print('page',page)
    # bookurls = []
    # bookurls = get_book_urls(page)
    # for bookurl in bookurls:
    #     filename = get_filename(bookurl)
    #     with open(filename,'a+',encoding='utf8') as f:
    #         f.write(bookurl)
