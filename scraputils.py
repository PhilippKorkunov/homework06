import requests
from bs4 import BeautifulSoup


def extract_news(parser):
    news_list=[]
    r=[]
    t=parser.body.center.table
    s=t.findAll("tr")
    for i in s:
        r.append(i)
    for i in range(0,len(r[3].findAll("tr"))-2,3):
        p=dict()
        c=r[3].findAll("tr")
        l=c[1+i]
        l=l.findAll("td")[1]
        l=l.findAll("a")
        if len(l)<4:
            continue
        k=c[1+i].findAll("td")[1]
        k=k.span
        k=k.text.split()[0]
        a=l[0].text
        p["points"]=int(k)
        p["author"]=a
        comm=""
        if len(l)==4:
            comm = l[3].text.split()
            comm=comm[0]
        if comm=="discuss" or len(comm)==0:
            p["comments"]=0
        elif len(comm)!=0:
            p["comments"]=int(comm)
        l1=c[i].findAll("td")
        l1=l1[2]
        l1=l1.find("a")
        p["title"]=l1.text
        p["url"]=l1["href"]
        news_list.append(p)
    return news_list


def extract_next_page(parser):
    r=[]
    t=parser.body.center.table
    s=t.findAll("tr")
    for i in s:
        r.append(i)
    if len(r[3].findAll("tr"))<92:
        return "newtest"
    c=r[3].findAll("tr")
    c=c[-1].findAll("td")[1]
    k=c.find("a")["href"]
    return k
           
    

def get_news(url, n_pages=1):
    """ Collect news from a given web page """
    news = []
    while n_pages:
        print("Collecting data from page: {}".format(url))
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        news_list = extract_news(soup)
        next_page = extract_next_page(soup)
        url = "https://news.ycombinator.com/" + next_page
        news.extend(news_list)
        n_pages -= 1
    return news