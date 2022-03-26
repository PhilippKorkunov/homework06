from bottle import (
    route, run, template, request, redirect
)

from scrapper import get_news
from db import News, session
from bayes import NaiveBayesClassifier


@route("/news")
def news_list():
    s = session()
    rows = s.query(News).filter(News.label == None).all()
    return template('news_template', rows=rows)


@route("/add_label/")
def add_label():
    l=requets.query["label"]
    i=request.query["id"]
    s=session()
    p=s.query(News).get(i)
    p.l=l
    s.add(p)
    s.commit()
    redirect("/news")


@route("/update")
def update_news():
    s=session()
    p=get_news("https://news.ycombinator.com/newest",1)
    for i in range(len(p)):
        news=News(title=p[i]["title"],author=[i]["author"],comments=p[i]["comments"],points=p[i]["points"],url=p[i]["url"])
        if s.query(News).filter(News.title == news.title and News.author == news.author).count()==0:
            s.add(news)
    s.commit()
    redirect("/news")


@route("/classify")
def classify_news():
    pass


if __name__ == "__main__":
    run(host="localhost", port=8080)

