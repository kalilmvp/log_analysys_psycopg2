import psycopg2

DB_HOST = '127.0.0.1'
DB_NAME = 'news'
DB_USER = 'vagrant'


def connection():
    return psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER)


def cursor(conn):
    return conn.cursor()


def question_1(conn, curs):
    curs.execute('select article_title, access_count from popular_articles')

    data = curs.fetchall()

    q = """
Question 1. What are the most popular three articles of all time? Which articles
have been accessed the most? Present this information as a sorted list with
the most popular article at the top
"""

    print(q)
    print("-" * 100)

    for (article_title, access_count) in data:
        print("    {} - {}".format(article_title, access_count))

    print("-" * 100)


def question_2(conn, curs):
    curs.execute('select author, page_views from popular_author')

    data = curs.fetchall()

    q = """
Question 2. Who are the most popular author of all time? That is, when you
sum up all of the articles each author has written, which authors get
the most page views? Present this as a sorted list with the most popular
author at the top.
"""

    print(q)
    print("-" * 100)

    for (author, page_views) in data:
        print("    {} - {}".format(author, page_views))

    print("-" * 100)


def question_3(conn, curs):
    curs.execute('select error_time, lead_errors from lead_errors_rate  where lead_errors > 1')

    data = curs.fetchall()

    q = """
Question 3. On which days did more than 1% of requests lead to errors? The log table includes
a column status that indicates the HTTP status code that the news site sent to the
user's browser. (Refer to this lesson for more information about the idea of HTTP
status codes.)
"""

    print(q)
    print("-" * 100)

    for (error_time, lead_errors) in data:
        print("    {} - {}%".format(error_time, lead_errors))

    print("-" * 100)


def main():
    conn = connection()
    curs = cursor(conn)

    question_1(conn, curs)
    print("*" * 100)
    question_2(conn, curs)
    print("*" * 100)
    question_3(conn, curs)

    curs.close()
    conn.close()


if __name__ == "__main__":
    main()
