import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
# from threading import Thread
# import time
from multiprocessing import Pool

def pre(withN):
    for i in range (len(withN)):
        withN[i] = withN[i].strip('\n')
    
    return withN

def check(name):
    html = urlopen(f"https://t.me/{name}").read()
    soup = BeautifulSoup(html, "html.parser")
    name = name.strip('\n')
    if soup.find_all("div","tgme_page_title") :
        # print(name, ": True")
        return True
    else:
        # print(name, ": False")
        return False
    
if __name__ == "__main__":
    # start = time.perf_counter()
    names = pre(open("names.txt", "r").readlines())

    with Pool(5) as p:
        res = p.map(check,names)

    for i in range(len(res)):
        print(names[i],":",res[i])

    # finish = time.perf_counter()
    # print("TIME : ", finish-start)
