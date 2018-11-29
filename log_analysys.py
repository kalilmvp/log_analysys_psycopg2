#!/usr/bin/env python3

import psycopg2

DB_HOST = '127.0.0.1'
DB_NAME = 'news'
DB_USER = 'vagrant'


def db_connection():
    """
    Creates and returns a connection to the database defined by DB_NAME,
    as well as a cursor for the database.

    Returns:
       conn, curs - a tuple.
        - The first element is a connection to the database.
        - The second element is a cursor for the database.
    """
    try:
        # conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER)
        conn = psycopg2.connect(dbname=DB_NAME)
        return conn, conn.cursor()
    except psycopg2.DatabaseError as e:
        print('Error when trying to open a connection: {}'.format(e))


def exec_query(sql):
    conn, curs = db_connection()

    curs.execute(sql)

    result = curs.fetchall()

    curs.close()
    conn.close()

    return result


def question_1():
    """
        Output the result of Question 1 for the project.
        Access the view 'popular_articles' and showcase the
        'article_title' and 'access_count'.
    """

    data = exec_query("""SELECT article_title, access_count
                        FROM popular_articles""")

    print("""1. What are the most popular three articles of all time?""")

    print("-" * 100)

    for (article_title, access_count) in data:
        print("    {} - {} views".format(article_title, access_count))

    print("-" * 100)


def question_2():
    """
        Output the result of Question 1 for the project.
        Access the view 'popular_author' and showcase the
        'author' and 'page_views'.
    """

    data = exec_query("""SELECT author, page_views
                         FROM popular_author""")

    print("""2. Who are the most popular article authors of all time?""")

    print("-" * 100)

    for (author, page_views) in data:
        print("    {} - {} views".format(author, page_views))

    print("-" * 100)


def question_3():
    """
        Output the result of Question 3 for the project.
        Access the view 'lead_errors' and showcase the
        'error_time' and 'lead_errors'.
    """

    data = exec_query("""
        SELECT to_char(error_time, 'Mon DD, YYYY'), lead_errors
        FROM lead_errors_rate
        WHERE lead_errors > 1
        """)

    print("""3. On which days did more than 1% of requests lead to errors?""")

    print("-" * 100)

    for (error_time, lead_errors) in data:
        print("    {} - {}%".format(error_time, lead_errors))

    print("-" * 100)


def main():
    question_1()
    print("*" * 100)
    question_2()
    print("*" * 100)
    question_3()


if __name__ == "__main__":
    main()
