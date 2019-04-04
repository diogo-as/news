# This Python file uses the following encoding: utf-8

import newsdb

a = newsdb.get_topArticles()
print ("Os 3 artigos mais lidos são: ")
for i in a:
    print i

b = newsdb.get_topAuthors()
print ("Os 3 autores com artigos mais lidos são: ")
for i in b:
    print i

c = newsdb.get_topError()
print ("O dia que houve mais erros de acesso: ")
for i in c:
    print table.apped.row[i]



#print(get_topAuthors())

#print(get_topError())
