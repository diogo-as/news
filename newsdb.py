# This Python file uses the following encoding: utf-8

import psycopg2

# função que retorna os tres artigos mais lidos de todos os tempos


def get_topArticles():
    try:
        db = psycopg2.connect("dbname=news")
        c = db.cursor()
        c.execute("select a.title, totals.views from articles a join (select substring, count(*) as views from shortlog group by substring) as totals on a.slug = totals.substring order by totals.views desc limit 3;")
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
        c.execute("select a.name, sum(b.views) as total_views from authors a join viewsArticles b on a.id = b.author group by a.name order by total_views desc limit 3;")
        return c.fetchall()
    except:
        print("Impossível conectar")
    finally:
        if(db):
            c.close()
            db.close()

# função retorna dia que houve mais erros de acesso


def get_topError():
    try:
        db = psycopg2.connect("dbname=news")
        c = db.cursor()
        c.execute("select a.data, a.total_ok, b.total_erros from accessok a join accesserror b on a.data = b.data;")
        return c.fetchall()
    except:
        print("Impossível conectar")
    finally:
        if(db):
            c.close()
            db.close()
