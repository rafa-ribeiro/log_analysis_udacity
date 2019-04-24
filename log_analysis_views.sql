-- Top articles views - lista os artigos que mais foram visualizados.
create view top_articles AS 
     select a.title as Article, count(*) as Views 
     from log l 
     join articles a on l.path = CONCAT('/article/', a.slug) 
     group by a.title, a.author 
     order by Views desc;


-- Top authors views
create view top_authors AS 
     select aut.name as Author, count(*) as Views 
     from log l 
     join articles a on l.path = CONCAT('/article/', a.slug) 
     join authors aut on aut.id = a.author
     group by a.author, aut.name 
     order by Views desc;

-- Query para buscar todas as requisições que ocorreram em um status diferente do '200 OK', ou seja, que resultaram em erro agrupados por dia.
create view errors_requests_per_day AS 
     select DATE(l.time) as day, count(*) as errors 
     from log l 
     where l.status <> '200 OK' 
     group by day;


-- Query para buscar o total de requisições realizadas agrupadas por dia.
create view total_requests_per_day AS 
     select DATE(l.time) as day, count(*) as total 
     from log l 
     group by day;


-- Query para retornar o percentual de requisições que resultaram em erros agrupadas por dia.
create view percent_errors_requests AS 
    select TO_CHAR(e.day, 'Mon DD, YYYY') as day, round(CAST(CAST(e.errors*100 AS float)/CAST(t.total AS float) AS numeric), 2) as percent_errors 
    from errors_requests_per_day as e, 
         total_requests_per_day as t 
    where e.day = t.day;