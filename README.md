# Project Log Analysys

This is a project number 3 of udacity Fullstack course. The purpose is a log analysys answering 3 main questions:
- Top 3 popular articles;
- Top 3 authors by number of views;
- Days with request erros equals or greater than 1%.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See requirements for notes on how to deploy the project on a live system.

### Requirements

To run this program you will need to install these structure:
  - [Vagrant](https://www.vagrantup.com/downloads.html)
  - [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

#### Config PostgreSQL (user, database schema)
To run de code you will nedd to download de database on [newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
Download and decompress the file.

##### Importind DB
To import database, on the directory do:

<code>$ psql -d news -f news_sql_database_file </code>


#### Creating DB table views
You need to create some table views to run the code. To do this, run the code below to create views from file createviews.sql:

 <code>$ psql -d news -f createviews.sql</code>

#### Dependencies

 [Tabulate](https://pypi.org/project/tabulate/)
 How to install:
 <code>$ pip install tabulate </code>

#### Project files
  - newsdb.py - DB conection and functions to get the results
  - news.py - Responsable for call de DB funcions, print the result and do some data manipulation
  - result.txt - print of execution of news.py
  - createviews.sql - Create views used by newsde.py

### Running

To execute the code just run the news.py file

<code>$ python news.py </code>

#### Output result example:

Top 3 popular articles:
Article                             Views
--------------------------------  -------
Candidate is jerk, alleges rival   338647
Bears love berries, alleges bear   253801
Bad things gone, say good people   170098

Top 3 authors by number of views:
Author                              Total Views
--------------------------------  -------------
Candidate is jerk, alleges rival         338647
Bears love berries, alleges bear         253801
Bad things gone, say good people         170098

Days with request erros equals or greater than 1%
Day           % Errors
----------  ----------
2016-07-17        2.32

## Changelog

v1.0 Version submitted to the first evaluation
v1.1 Updated by the first evaluation

## Contribute

If you have any suggestions or bug reports, Please create a Issue.

Pull Requests are always welcome.
