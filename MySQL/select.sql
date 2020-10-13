-- Christopher Nolan 導演過幾部電影?
-- select count(*) from movie where director_name='Christopher Nolan';
-- Tom Hardy 出演過幾部電影?
-- select count(*) from movie where actor_1_name='Tom Hardy' or actor_2_name='Tom Hardy';
-- 一共有多少導演?
-- select count(distinct director_name) from movie;
-- Top 5 拍電影最多的導演
-- select  director_name, count(title) from movie group by director_name order by count(title) desc limit 5;
-- Top 5 歷史總票房最高的導演
select director_name, sum(gross), count(title), avg(gross) from movie group by director_name order by sum(gross) desc limit 5;
-- Top 5 歷史平均票房最高的導演
select director_name, sum(gross), count(title), avg(gross) from movie group by director_name order by avg(gross) desc limit 5;