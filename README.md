## Logs Analysis Project for FullStack Developer NanoDegree

This project is intented to execute certain sql scripts at a mock PostgreSQL
database to display data about a news program. The python script uses *psycopg2* library 
to query the database and produce a report that answers the following three questions:


#### Questions
1. What are the most popular three articles of all time?
  Which articles have been accessed the most?
  Present this information as a sorted list with the most popular article at the top
2. Who are the most popular article authors of all time?
  That is, when you sum up all of the articles each author has written, which authors get the most page views?
  Present this as a sorted list with the most popular author at the top.
3. On which days did more than 1% of requests lead to errors?
  The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

### Requirements
* Python 3.7
* Postgresql 9

### How to run
* You need to be using a Python version >= 3
* Add all the dependencies from requirements.txt 
```
pip install -r requirements.txt
```
* Download the Docker image with everything needed to run and create 
thd database for news schema:
```
https://github.com/albertoivo/docker-fullstacknd
```
* Need to create all the views necessary for the software to run.
Just use the file **create_views.sql** at this folder and run with
the following command at your Postgres console:
```sql
psql -d news -f create_views.sql
```
* Run the software
```
python3 log_analysys.py
``` 




