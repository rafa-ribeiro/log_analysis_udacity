# Database access code for the News DB on Vagrant Virtual Machine.

import psycopg2

# TOP_ARTICLES_VIEW = "select a.title as Article, count(*) as Views from log l join articles a on l.path = CONCAT('/article/', a.slug) group by a.title order by Views desc"

TOP_ARTICLES_VIEW_NAME = "top_articles"
TOP_ARTICLES_VIEW = "create view %s AS select a.author, a.title as Article, count(*) as Views from log l join articles a on l.path = CONCAT('/article/', a.slug) group by a.title, a.author order by Views desc" % TOP_ARTICLES_VIEW_NAME

def top_three_articles():
    query = "select t.article, t.views from top_articles t limit 3"

    db = connect_db()
    c = db.cursor()
    c.execute(query)
    return c.fetchall()
    db.close()

def top_authors_most_popuplar():
    query = "select a.name, t.views from authors a join top_articles t on t.author = a.id"

    db = connect_db()
    c = db.cursor()
    c.execute(query)
    return c.fetchall()
    db.close()


def days_with_more_errors_request():
    query = "select result.day, result.percent_errors from percent_errors_requests as result where result.percent_errors > 1;"

    db = connect_db()
    c = db.cursor()
    c.execute(query)
    return c.fetchall()
    print("Fechando conexao com banco.")
    db.close()


def initialize_views():
    db = connect_db()
    check_view(db, TOP_ARTICLES_VIEW_NAME)
    db.close()

def check_view(db, view_name):
    c = db.cursor()

    count_query = ("select count(*) from INFORMATION_SCHEMA.views where table_name = '%s'" % view_name)
    c.execute(count_query)
    count = c.fetchone()[0]

    print("Checando view '%s'" % view_name)
    if (count == 1):
        print("View OK." % view_name)
    else:
        c.execute(TOP_ARTICLES_VIEW)
        db.commit()
        print("View nao encontrada. Criando view...")

def connect_db():
    """Connect to database"""
    db = psycopg2.connect("dbname=news")
    return db