## Logs Analysis Project for FullStack Developer NanoDegree

### Questions
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
* Need to create all the views necessary for the software to run
```
create view popular_articles as
  select art.title as article_title,
         count(l.path) as access_count
  from log as l join articles as art on l.path = CONCAT('/article/', art.slug)
  where l.status = '200 OK'
  group by art.title order by access_count desc limit 3;
```
```
create view popular_author as
   select auth.name as author,
         count(l.path) as page_views
  from log as l join articles as art on l.path = CONCAT('/article/', art.slug)
      join authors as auth on auth.id = art.author
  where l.status = '200 OK'
  group by auth.name
   order by page_views desc;
```
```
create view request_errors as
  SELECT l.time::date, COUNT(*) AS page_views_errors
  FROM log as l
  where l.status != '200 OK'
  GROUP BY l.time::date
  ORDER BY l.time::date;
```
```
CREATE VIEW page_views_grouped AS
  SELECT l.time::date, COUNT(*) AS page_views
  FROM log as l
  GROUP BY l.time::date
  ORDER BY l.time::date;
```
```
CREATE VIEW lead_errors_rate AS
  SELECT pvg.time::date as error_time,
         ROUND((100.0 * re.page_views_errors / pvg.page_views)::numeric, 2) AS lead_errors
  FROM page_views_grouped pvg join request_errors re on re.time::date = pvg.time::date
  ORDER BY pvg.time::date;
```
* Run the software
```
py log_analysys.py
``` 




