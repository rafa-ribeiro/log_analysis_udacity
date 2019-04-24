# Database access code for the News DB on Vagrant Virtual Machine.

import psycopg2

views = ["top_articles", "top_authors", "errors_requests_per_day",
         "total_requests_per_day", "percent_errors_requests"]


def top_three_articles():
    query = "select t.article, t.views from top_articles t limit 3"

    db = connect_db()
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()

    print("%s | %s" % ('Articles'.ljust(50), 'Views'))
    for row in result:
        print("%s | %s" % (row[0].ljust(50), row[1]))
    print("\n")


def top_authors_most_popuplar():
    query = "select ta.author, ta.views from top_authors ta"

    db = connect_db()
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()

    print("%s | %s" % ('Name'.ljust(50), 'Views'))
    for row in result:
        print("%s | %s" % (row[0].ljust(50), row[1]))
    print("\n")


def days_with_more_errors_request():
    query = "select result.day, result.percent_errors " \
            "from percent_errors_requests as result " \
            "where result.percent_errors > 1"

    db = connect_db()
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()

    print("%s | %s" % ('Day'.ljust(50), 'Percent errors'))
    for row in result:
        print("%s | %s" % (str(row[0]).ljust(50), row[1]))
    print("\n")


def check_views():
    db = connect_db()
    check_views_exists(db)
    db.close()


def check_views_exists(db):
    c = db.cursor()
    for view in views:
        count_query = "select count(*) from INFORMATION_SCHEMA.views " \
                      "where table_name = '%s'" % view

        c.execute(count_query)
        count = c.fetchone()[0]
        if (count == 0):
            msg = "Error. View '%s' not found. Please, execute the create" \
                "views described in file 'log_analysis_views.sql'." % view
            raise Exception(msg)


def connect_db():
    """Connect to database"""
    db = psycopg2.connect("dbname=news")
    return db
