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
            formatedtext = soup.get_text(separator=" ", strip=True).replace("From Wikipedia, the free encyclopedia Jump to navigation Jump to search","").replace("Wikipedia","").replace("Jump to search","").replace("Jump to navigation","")
            saintdict[saintkey] = {"saint": saintkey,"link": url, "text": resp.text, "formatedtext": formatedtext}
            with open(f'saints/{saintkey}.json','w', encoding="utf-8") as w:
                w.write(json.dumps(saintdict[saintkey],indent=2))
            print(f"Success GET {saintkey}")
        else:
            print(f"{saintkey} is a place: {isplace}")
    except Exception as e:
        errorlist.append(f"Error {saintkey} {e}")
        print(f"Error {saintkey} {e}")


if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        saintset = set()
        with open('saintsraw.txt', 'r', errors='ignore') as r:
            saintset = set(line for line in r.read().split('\n'))
        cs = 1 + (len(saintset)//8)
        executor.map(saint, saintset, chunksize=cs)
    print(f"size:{len(os.listdir('saints'))}")

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