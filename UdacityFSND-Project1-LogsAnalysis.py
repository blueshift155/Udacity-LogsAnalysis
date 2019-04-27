#!/usr/bin/env python

import psycopg2

DBNAME = "news"

# Queries for the reporting tool

query_populararticle = """
SELECT title, count(*) as views FROM articles
JOIN log
ON articles.slug = substring(log.path, 10)
WHERE status='200 OK'
GROUP BY title ORDER BY views DESC LIMIT 3;
"""

query_popularauthor = """
SELECT authors.name, count(*) as views
FROM articles
JOIN authors
ON articles.author = authors.id
JOIN log
ON articles.slug = substring(log.path, 10)
WHERE status='200 OK'
GROUP BY authors.name ORDER BY views DESC;
"""

query_errors = """
SELECT errorcountsbyday.date, round(100.0*errorcount/logcount,2) as percent
FROM logcountsperday, errorcountsbyday
WHERE logcountsperday.date = errorcountsbyday.date
AND errorcount > logcount/100;
"""

# Connect to the database and input query to return results


def get_queryResults(sql_query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(sql_query)
    results = c.fetchall()
    db.close()
    return results

# Store results


result1 = get_queryResults(query_populararticle)

result2 = get_queryResults(query_popularauthor)

result3 = get_queryResults(query_errors)


# Create a function to print query results


def print_results(q_list):

    for i in range(len(q_list)):
        title = q_list[i][0]
        res = q_list[i][1]
        print("\t" + "%s - %d" % (title, res) + " views")
        print("\n")


print("What are the most popular articles of all time?")

print_results(result1)

print("Who are the most popular article authors of all time?")

print_results(result2)

print("On which days more than 1% of the requests led to error?")

print("\t" + str(result3[0][0]) + " - " + str(result3[0][1]) + "% errors")
