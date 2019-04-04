# This Python file uses the following encoding: utf-8

import psycopg2

#função que retorna os tres artigos mais lidos de todos os tempos
def get_topArticles ():
    try:
        db = psycopg2.connect("dbname=news")
        c = db.cursor()
#        c.execute("create view shortlog as select substring(path,10,50) from log where status = '200 OK'")
        c.execute("select a.author, a.title, totals.views from articles a join (select substring, count(*) as views from shortlog group by substring) as totals on a.slug = totals.substring order by totals.views desc limit 3;")
        return c.fetchall()
    except:
        print("Impossível conectar")
    finally:
        if(db):
            c.close()
            db.close()

# função que retorna os autores dos artigos mais populares
def get_topAuthors():
    try:
        db = psycopg2.connect("dbname=news")
        c = db.cursor()
        # create view top3articles as select a.author, a.title, totals.views from articles a join (select substring, count(*) as views from shortlog group by substring) as totals on a.slug = totals.substring order by totals.views desc limit 3;
        c.execute("select a.name from authors a join top3articles b on a.id = b.author;")
        return c.fetchall()
    except:
        print("Impossível conectar")
    finally:
        if(db):
            c.close()

# função retorna dia que houve mais erros de acesso
def get_topError():
    try:
        db = psycopg2.connect("dbname=news")
        c = db.cursor()
        c.execute("select count(*) as qnt_erros, date(time) from log where status != '200 OK' group by date(time) order by qnt_erros desc limit 1;")
        return c.fetchall()
    except:
        print("Impossível conectar")
    finally:
        if(db):
            c.close()
