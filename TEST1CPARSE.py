# -*- coding: utf-8 -*-
import requests
import os
from bs4 import BeautifulSoup
from tqdm import tqdm
login = input("Введите логин")
password = input("Введите пароль")
def down(elem):
    file = sess.get(elem[2], stream = 'true')
    size = int(file.headers.get('Content-Length'))
    filename = file.headers.get('Content-Disposition')[file.headers.get('Content-Disposition').find("=") + 2:-1]
    print(os.getcwd() + "\\conf" + "\\" + elem[0] + "\\" + elem[1])
    try:
        os.makedirs(os.getcwd() + "\\conf" + "\\" + elem[0] + "\\" + elem[1])
    except:
        pass
    namepath = os.getcwd() + "\\conf" + "\\" + elem[0] + "\\" + elem[1] + "\\" + filename
    with open(namepath, 'wb') as f:
        for data in tqdm(iterable = file.iter_content(chunk_size = 1024), total = size/1024, unit = 'KB'):
            f.write(data)
        f.close
    with open(os.getcwd() + "\\conf" + "\\Log.txt",'a') as f:
        f.write(elem[0] + ":" + elem[1] + "\n")
        f.close
    print("Создан " + os.getcwd() + "\\conf" + "\\" + elem[0] + "\\" + elem[1] + "\\" + filename)
global sess
sess = requests.Session()
data = {
'inviteCode':'',
'username':login,
'password':password,
'execution':BeautifulSoup(sess.get('https://login.1c.ru/login').content,"html.parser").findAll('input')[3].attrs.get('value'),
'_eventId':'submit',
'geolocation':'',
'submit':'Войти',
'rememberMe':'on'}
sess.post('https://login.1c.ru/login',data=data)
url2 = "https://releases.1c.ru"    
bon = BeautifulSoup(sess.get(url2 + '/total').content,"html.parser")
bs = bon.find("tbody").findAll("tr")
konfi = ('Управление торговлей, редакция 11','Комплексная автоматизация, редакция 2','Комплексная автоматизация, редакция 1.1','Бухгалтерия предприятия, редакция 2.0','Бухгалтерия предприятия, редакция 3.0','Зарплата и Управление Персоналом, редакция 2.5','Зарплата и Управление Персоналом, редакция 3',"Технологическая платформа 8.3")
konf = []
def href(z):
    td[0] = z
    return(str(td[0].a)[str(td[0].a).find("href") + 6:str(td[0].a).find('>') - 1].replace('amp;',''))
for i in range(6,len(bs) + 1):
    try:
        if bs[i].find("td").text.strip() in konfi:
            td = bs[i].findAll('td')
            konf.append([td[0].text.strip(),td[1].text.strip(),href(td[0])])
    except:
        pass
print('Поиск обновлений')
for elem in konf:
    vers = href(BeautifulSoup(sess.get(url2 + elem[2]).content,"html.parser").find('td',class_="versionColumn"))
    for i in BeautifulSoup(sess.get(url2+vers).content,"html.parser").findAll('div',class_='formLine'):
        if i.text.strip() == "Дистрибутив обновления" or i.text.strip() == "Технологическая платформа 1С:Предприятия для Windows":
            elem[2] =(href(BeautifulSoup(sess.get(url2 + href(i)).content,"html.parser").find('div',class_='downloadDist')))
        if i.text.strip() == "Полный дистрибутив":
            elem[2] =(href(BeautifulSoup(sess.get(url2 + href(i)).content,"html.parser").find('div',class_='downloadDist')))
for elem in konf:
    try:
        with open(os.getcwd() + "\\conf" + "\\Log.txt", 'r') as f:
            for line in f:
                if elem[0] in line:    
                    vers = line[line.find(elem[0]) + len(elem[0]) + 1:-1]
                    print(vers)
            f.close
        if elem[1] != vers:
            down(elem)
        print("По " + elem[0] + " обновлений не найдено")
    except:
        down(elem)
with open(os.getcwd() + "\\conf" + "\\Log.txt", 'w') as f:
    f.close
for elem in konf:
    with open(os.getcwd() + "\\conf" + "\\Log.txt", 'a') as f:
        f.write(elem[0]+":"+ elem[1] + "\n")
        f.close
a = input("Нажмите любую клавишу ")



