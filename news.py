#!/usr/bin/env python
# This Python file uses the following encoding: utf-8


import newsdb
from beautifultable import BeautifulTable


topArticles = newsdb.get_topArticles()
table = BeautifulTable()
print ("Top 3 popular articles: ")
table.column_headers = ["Article", "Views"]
for row in topArticles:
    table.append_row(row)
print table

topAuthors = newsdb.get_topAuthors()
table = BeautifulTable()
table.column_headers = ["Author", "Total Views"]
print ("Top 3 authors by number of views: ")
for row in topAuthors:
    table.append_row(row)
print table

topError = newsdb.get_topError()
table = BeautifulTable()
table.column_headers = ["Day", "Erros", "Acess OK"]
print ("Days with request erros equals or greater than 1% ")
for row in topError:
    error = float(row[2])
    ok = float(row[1])
    media = (error/ok)*100
    if media >= 1:
        table.append_row(row)
print table
