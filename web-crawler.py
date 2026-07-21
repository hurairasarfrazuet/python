import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
url=input('Enter - ')
if len(url)<1:
    print('Empty URL')
    quit()
if not url.__contains__('http') and not url.__contains__('https'):
    urls=[f'http://{url}', f'https://{url}']
else:
    urls=[url]
try:
    html=urllib.request.urlopen(urls[0]).read()
except:
    try:
        html=urllib.request.urlopen(urls[1]).read()
    except Exception as e:
        print('Error:', e)
        quit()
soup=BeautifulSoup(html,'html.parser')
tags=soup('a')
count=0
for tag in tags:
    href=tag.get('href',None)
    if not href is None and not href.startswith('#'):
        print(href)
        count+=1
print('Total Links:',count)
