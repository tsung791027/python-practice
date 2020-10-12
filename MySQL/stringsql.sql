--SELECT title, CHAR_LENGTH(title) as chracter_count from movie;
SELECT CONCAT(substr(title,1,8), "...") as short_title, director_name from movie;