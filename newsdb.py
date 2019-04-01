import pyscopg2



#função que retorna os tres artigos mais lidos de todos os tempos
def get_topArticles ():
    db = psycopg2.connect("dbname=news")
    c = db1.cursor()
    c.execute("Select content, time from posts order by time desc")
    return d.fetchall()
    db.close()


# função que retorna os autores dos artigos mais populares
def get_topAuthors():
    db = psycopg2.connect("dbname=news")
    c = db1.cursor()
    c.execute("Select content, time from posts order by time desc")
    return d.fetchall()
    db.close()



# função retorna dia que houve mais erros de acesso
def get_topError():
    db = psycopg2.connect("dbname=news")
    c = db1.cursor()
    c.execute("Select content, time from posts order by time desc")
    return d.fetchall()
    db.close()
