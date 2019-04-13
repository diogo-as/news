#!/usr/bin/env python
# This Python file uses the following encoding: utf-8


import newsdb
from tabulate import tabulate


topArticles = newsdb.get_topArticles()
print ("Top 3 popular articles: ")
print tabulate(topArticles, headers=["Article", "Views"])

topAuthors = newsdb.get_topAuthors()
print ("Top 3 authors by number of views: ")
print tabulate(topArticles, headers=["Author", "Total Views"])


topError = newsdb.get_topError()
resultlist = []
resultlist1 = []
for row in topError:
    error = float(row[2])
    ok = float(row[1])
    media = round((error/ok)*100, 2)
    if media >= 1:
        resultlist1.append(row[0])
        resultlist1.append(media)
        resultlist.append(resultlist1)

print ("Days with request erros equals or greater than 1% ")
print tabulate(resultlist, headers=["Day", "% Errors"])
