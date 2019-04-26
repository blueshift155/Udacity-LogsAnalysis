# Logs Analysis
This is the first project of the Udacity's Full Stack Web Development Nano-degree program. 

## Overview
The objective is to create and use SQL queries in Python code that outputs a report based on below questions from a mock database of a news website.

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Design
SQL queries for each of the individual questions above have been stored separately. The code makes use of the the `psycopg2` module to connect to the database and execute these queries to generate desired results. This is just the basic structure of program code.

In addition to this, to improve on the understanding level of this course and according to standard guidelines when developing a databased based software, SQL views are used in the algorithm for the third question. SQL view is a table in the form of a pre-defined SQL query which is commonly used for security purpose restricting the user from viewing certain rows and columns.

## Usage
#### Minimal Requirements
[Python 3](https://www.python.org/download/releases/3.0/)
[Psycopg2 module](https://pypi.org/project/psycopg2/)
[SQL dump of News database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

The script is to be run only on the machine that locally hosts the PostgreSQL database server. One must have knowledge of installing software packages, use the PIP package manager for Python and also importing SQL dumps to the database server.

#### Virtual Machine environment

If you don't want to manually setup the environment, it is recommended to follow instructions [here](https://github.com/udacity/fullstack-nanodegree-vm) to setup virtual machine required for running this Python script. This will setup the complete environment with Python and PostgreSQL server. You will just have to import the sql dumps in the server.

#### Creating SQL Views

Using any supported SQL client or `psql` utility, create the following views.

```plsql
CREATE VIEW logcountsperday AS
SELECT to_char(time,'MONTH DD, YYYY') as Date, count(*) as LogCount
FROM log
GROUP BY Date;
```

```plsql
CREATE VIEW errorcountsbyday AS
SELECT to_char(time,'MONTH DD, YYYY') as Date, count(*) as ErrorCount
FROM log
WHERE STATUS = '404 NOT FOUND'
GROUP BY Date;
```

#### Running the script

After environment is setup and views are properly created, use the Python command line tool to run the project script and view the reports generated in the terminal.

## Author

*Girish Thavai*

