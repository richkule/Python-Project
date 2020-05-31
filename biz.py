import time
import requests
from bs4 import BeautifulSoup
url = 'http://bizovo.ru/prodazha/auto'
def Id(href):
    i = 0
    for elem in href[-1:0:-1]:
        if elem !="-":
            i+=1
        else:
            break
    return href[-i:-5]
def wr(sp):
    with open('dt.txt','a') as f:
        for elem in sp:
            for elem2 in elem:
                f.write(elem2)
                f.write(';')
            f.write('\n')
        f.close()
def gor(a):
    i = 0
    for elem in a[-1:0:-1]:
        if elem.isupper():
            break
        else:
            i+=1
    return [a[0:-i-1],a[-i-1:]]
def pageparse(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html,'html.parser')
    alist = soup.findAll('tr')
    alist = alist[1:]
    spis = []
    for elem in alist:
        href = elem.find('a').attrs['href']
        ID = Id(href)
        cont = elem.contents
        lis = [ID]
        lis += gor(cont[2].text)
        if cont[7].text != "продано":
            lis.append(cont[7].text)
        else:
            continue
        lis += [time.ctime()]
        lis += [href]
        spis.append(lis)
    return spis
def lastpage(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html,'html.parser')
    li = soup.findAll('li')
    li = str(li[-2])
    li = li[li.find("Страница ")+10:]
    li = li[:li.find('"')]
    return int(li)
def parse(lpage,url):
    url = url + "?page="
    for i in range(1,lpage+1):
        print('Страница ' + str(i))
        wr(pageparse(url+str(i)))
ls = lastpage(url)
parse(ls,url)
        

        
