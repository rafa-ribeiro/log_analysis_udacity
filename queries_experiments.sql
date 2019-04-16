-- Top articles views
create view top_articles AS select a.author, a.title as Article, count(*) as Views from log l join articles a on l.path = CONCAT('/article/', a.slug) group by a.title, a.author order by Views desc;


-- Query única - 1 linha
select test.day, test.percent_errors from (select e.day, e.errors, t.total, round(CAST(CAST(e.errors*100 AS float)/CAST(t.total AS float) AS numeric), 2) as percent_errors from (select DATE(l.time) as day, count(*) as errors from log l where l.status <> '200 OK' group by day) as e, (select DATE(lo.time) as day, count(*) as total from log lo group by day) as t where e.day = t.day) as test where test.percent_errors > 1;


select test.day, test.percent_errors 
from (
    select e.day, e.errors, t.total, round(CAST(CAST(e.errors*100 AS float)/CAST(t.total AS float) AS numeric), 2) as percent_errors 
    from 
    (select DATE(l.time) as day, count(*) as errors 
        from log l where l.status <> '200 OK' group by day) as e, 
    (select DATE(lo.time) as day, count(*) as total 
        from log lo group by day) as t where e.day = t.day) as test 
where test.percent_errors > 1;


-- Query para buscar todas as requisições que ocorreram em um status diferente do '200 OK', ou seja, que resultaram em erro agrupoados por dia.
create view errors_requests_per_day as select DATE(l.time) as day, count(*) as errors from log l where l.status <> '200 OK' group by day;

-- Query para buscar o total de requisições realizadas agrupadas por dia.
create view total_requests_per_day as select DATE(l.time) as day, count(*) as total from log l group by day;


-- Query para retornar o percentual de requisições que resultaram em erros agrupadas por dia.
create view percent_errors_requests as 
    select e.day, round(CAST(CAST(e.errors*100 AS float)/CAST(t.total AS float) AS numeric), 2) as percent_errors 
    from errors_requests_per_day as e, 
         total_requests_per_day as t 
    where e.day = t.day;

-- Agrupando as views e executando-as
select result.day, result.percent_errors 
from percent_errors_requests as result 
where result.percent_errors > 1;