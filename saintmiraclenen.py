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
import string
if __name__ == '__main__':
    resp = "Don't say I didn't warn you. The gypsy profits have a book (ryhmes with falmud), in this book they claim that JC was the son of a whore and a roman soldier named pantera. They also say that JC is burning in a lake of s$!t and fire. What do we know about the gypsy profits? We know that they are masters at word spells(zionist, anti-semetic, racist). They use word spells to get around lying because if you outright lie the universe karmically corrects itself and the liar will receive righteous retribution in some form depending on the severity of the lie and the intent behind the lie. So why would the people known throughout the land for getting around lies with word spells say JC was the son of a rape and that JC is burning in a lake of siht and fire? If it was a lie they would likely all die in mysterious accidents within a month. If it was the truth but they used the name to represent a different man then its not technically a lie. JC is a word spell. The gypsy profits inserted the name Jesus Christ into the Bible to replace the real man who was probably named Jmmanuel. The name doesn't matter but the real man was 10x more based than what they tell you about him in the Bible. The pharisees used J's teachings to control the world, they did this by mixing 3 lies in with every 7 truths. The most important part about Christianity are the miracles, and most important part about the Bible is what it does to help people with a high level of perception to navigate their path of awakening to the Creator. Those two things are the cause for Christianity becoming the force thats proactive towards evil (until now), they are not the result of being proactive towards evil, they are the cause. If you want a much more accurate story about J but still not 100%, its about 80-90 percent accurate and reads like the book of matthew which was about 40-50 percent accurate, in fact the book of matthew was supposedly a grabbled copy of the falmud of J. The falmud of J(if I spell it out for you youtube censors my comment) has a pdf link on archive dot org. Are ya startin to figure out why I said that phrase twice?  Now for the third time Ill say it, You Are Not Your Beliefs."
    lowerletters = string.ascii_lowercase
    lines = set()
    lines = set(resp.split())
    print(isinstance(lines,set))

    # with open('saintset2', 'r', errors='ignore') as r:
    #     saintset = sorted(set([line for line in r.read().split('\n')]))
    # with open('saintset2', 'w') as w:
    #     w.write('\n'.join(saintset))
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