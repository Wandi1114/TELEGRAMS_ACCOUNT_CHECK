import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup


def check(name):
    html = urlopen(f"https://t.me/{name}").read()
    soup = BeautifulSoup(html, "html.parser")

    if soup.find_all("div","tgme_page_title") :
        return True
    else:
        return False
    

names = open("names.txt", "r")
# print(check("f23f23"))
# print(names.readlines()[0])
for name in names.readlines() :
    print(name.strip('\n'),":",check(name))
    # print(name.strip('\n'))
names.close()
