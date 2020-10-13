-- SELECT title, CHAR_LENGTH(title) as chracter_count from movie;

-- SELECT CONCAT(substr(title,1,8), "...") as short_title, director_name from movie;

-- SELECT title, director_name, title_year from movie where title like "%dark%"

-- SELECT 
--     title, title_year, director_name, gross, actor_1_name, actor_2_name 
--     from movie 
--     order by gross desc limit 10;

-- SELECT 
--     title, title_year, gross, imdb_score 
--     from movie 
--     where director_name='Peter Jackson' 
--     order by gross desc limit 1;

-- SELECT 
--     title, title_year, director_name 
--     from movie
--     order by title;

-- SELECT
--     title, title_year, imdb_score
--     from movie
--    where director_name='Christopher Nolan'
--     order by imdb_score desc
--     limit 1;

