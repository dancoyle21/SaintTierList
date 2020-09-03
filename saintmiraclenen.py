import requests,json,os
import concurrent.futures
from bs4 import BeautifulSoup

def saint(sk):
    saintkey = sk[6:]
    url = f"https://en.wikipedia.org/wiki/{saintkey}"
    try:
        saintdict,errorlist = {},[]
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content, 'lxml')
        isplace = soup.find('span',{'class':'geo-dms'})
        if not isplace:
            print(saintkey)
            with open(f'saints/{saintkey}.html', 'w', encoding='utf-8') as w:
                w.write(resp.text)
            print(f"Success GET {saintkey}")
        else:
            print(f"{saintkey} is a place: {isplace}")
    except Exception as e:
        errorlist.append(f"Error {saintkey} {e}")
        print(f"Error {saintkey} {e}")

import pdfkit

def html2pdf(wikisaint):
    saintkey = wikisaint
    url = f"https://en.wikipedia.org/wiki/{saintkey}"
    try:
        p = f"saints/{saintkey}.pdf"
        if os.path.isfile(p) and os.stat(p).st_size > 0:
            print(f"{saintkey} already exists")
        else:
            pdfkit.from_url(url, p)
            print(f"Success GET {saintkey}")
    except Exception as e:
        print(f"Error {saintkey} {e}")


def pdfbyalphabet(saintlist):
    try:
        letter = saintlist[0][0]
        print(letter)
        urls = [f"https://en.wikipedia.org/wiki/{s}" for s in saintlist]
        urlbyletter = []
        for u in urls:
            resp = requests.get(u)
            soup = BeautifulSoup(resp.content, 'lxml')
            isplace = soup.find('span',{'class':'geo-dms'})
            if not isplace:
                urlbyletter.append(u)

        # print(urlbyletter)
        
        p = f"saintsbyalphabet{letter}.pdf"
        # if os.path.isfile(p) and os.stat(p).st_size > 0:
        #     print(f"{letter} already exists")
        # else:
        pdfkit.from_url(urlbyletter,p, options={"--javascript-delay": 20000})
        print(f"Success GET letter: {letter}")
    except Exception as e:
        print(f"Error {e}")

def rewritesaintset(saint):
    u = f"https://en.wikipedia.org/wiki/{saint}"
    print(f"url:{u}")
    try:
        resp = requests.get(u)
        soup = BeautifulSoup(resp.content, 'lxml')
        isplace = soup.find('span',{'class':'geo-dms'})
        if not isplace:
            with open('saintset2', 'a') as w:
                w.write(f"{saint}\n")
            print(f"success: {u}")
        else:
            print(f"isplace: {u}")
    except Exception as e:
        print(f"error: {u} {e}")



from itertools import groupby
if __name__ == '__main__':
    with open('saintset2', 'r', errors='ignore') as r:
        saintset = sorted(set([line for line in r.read().split('\n')]))
    with open('saintset2', 'w') as w:
        w.write('\n'.join(saintset))
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     with open('saintset', 'r', errors='ignore') as r:
    #         saintset = sorted(set([line for line in r.read().split('\n')]))
    #     print(saintset)
    #     cs = len(saintset)//os.cpu_count()
    #     executor.map(rewritesaintset, saintset, chunksize=cs)


    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     saintset = set()
    #     with open('saintset', 'r', errors='ignore') as r:
    #         saintset = sorted(set([line for line in r.read().split('\n')]))
    #     print(f"length saintset:{len(saintset)}")
    #     groupedsaints = {k:list(g) for k, g in groupby(saintset, key=lambda x: x[0].upper())}
    #     # print(groupedsaints)
    #     cs = len(groupedsaints)//os.cpu_count()
    #     executor.map(pdfbyalphabet, groupedsaints.values(), chunksize=cs)
    # print(f"size:{len(os.listdir('saints'))}")

# def all_saints():
#     saintlist = []
#     with open('saintsraw.txt', 'r', errors='ignore') as r:
#         saintlist = [line for line in r.read().split('\n')]
#     saintdict,errorlist = {},[]
#     for sc in set(saintlist):
#         saintkey = sc[6:]
#         url = f"https://en.wikipedia.org/wiki/{saintkey}"
#         try:
#             resp = requests.get(url)
#             soup = BeautifulSoup(resp.content, 'lxml')
#             isplace = soup.find('span',{'class':'geo-dms'})
#             if isplace:
#                 print(f"{saintkey} is a place: {isplace}")
#                 continue
#             print(saintkey)
#             saintdict[saintkey] = {"saint": saintkey,"link": url, "body": str(soup.find_all('p')), "text": soup.get_text(separator=" ", strip=True)}
#             with open(f'saints/{saintkey}.json','w', encoding="utf-8") as w:
#                 w.write(json.dumps(saintdict[saintkey],indent=2))
#             print(f"Success GET {saintkey}")
#         except Exception as e:
#             errorlist.append(f"Error {saintkey} {e}")
#             print(f"Error {saintkey} {e}")
#     print("errorlist: " +errorlist)
# # all_saints()

# def fmtsaints():
#     jdict = {}
#     for f in os.listdir("saints"):
#         try:
#             print(f)
#             with open(f"./saints/{f}", 'r') as r:
#                 jdict = json.load(r)
#             with open(f"./saints/{f}", 'w') as w:
#                 w.write(json.dumps(jdict,indent=2))
#         except FileNotFoundError as fnfe:
#             print(fnfe)
# # fmtsaints()
# # print(len(os.listdir("saints")))