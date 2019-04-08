# Project Log Analysys

This is a project number 3 of udacity Fullstack course. The purpose is a log analysys answering 3 main questions:
- Top 3 popular articles;
- Top 3 authors by number of views;
- Days with request erros equals or greater than 1%.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Project files
  - newsdb.py - DB conection and functions to get the results
  - news.py - Responsable for call de DB funcions, print the result and do some data manipulation

### Prerequisites

#### Creating DB table views

You need to create 2 table views to run the code:

<code>$ create view shortlog as select substring(path,10,50) from log where status = '200 OK'</code>

 <code>$ create view viewsArticles as select a.author, totals.views from articles a join (select substring, count(*) as views from shortlog group by substring) as totals on a.slug = totals.substring;</code>

#### Dependencies

 BeautifulTable package <https://github.com/pri22296/beautifultable>.

 How to install:
 <code>$ pip install beautifultable </code>

### Running

To execute the code just run the news.py file

<code>$ python news.py </code>

#### Output result example:

- Top 3 popular articles:

|             Article              | Views  |
|----------------------------------|--------|
| Candidate is jerk, alleges rival | 338647 |
| Bears love berries, alleges bear | 253801 |
| Bad things gone, say good people | 170098 |

- Top 3 authors by number of views:

|         Author         | Total Views |
|------------------------|-------------|
|    Ursula La Multa     |   507594    |
| Rudolf von Treppenwitz |   423457    |
| Anonymous Contributor  |   170098    |

- Days when request erros equals or greater than 1%:

|    Day     | Erros | Acess OK |
|------------|-------|----------|
| 2016-07-17 | 54642 |   1265   |


## Changelog

v1.0 Version submitted to the first evaluation

## Contribute

If you have any suggestions or bug reports, Please create a Issue. 

Pull Requests are always welcome.

