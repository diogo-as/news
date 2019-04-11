create or replace view shortlog as select substring(path,10,50) from log where status = '200 OK';
create or replace view viewsArticles as select a.author, totals.views from articles a join (select substring, count(*) as views from shortlog group by substring) as totals on a.slug = totals.substring;
create or replace view accesserror as SELECT date (a."time") AS data, count(*) AS total_erros FROM log a WHERE a.status <> '200 OK'::text GROUP BY (date(a."time"));
create or replace view accessok as SELECT date(a."time") AS data, count(*) AS total_ok FROM log a WHERE a.status = '200 OK'::text GROUP BY (date(a."time"));
