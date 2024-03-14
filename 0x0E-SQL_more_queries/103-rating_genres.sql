-- List all genres in the database hbtn_0d_tvshows_rate by their rating sum
SELECT a.name, SUM(c.rate) AS rating
FROM tv_genres AS a
INNER JOIN tv_show_genres AS b ON b.genre_id = a.id
INNER JOIN tv_show_ratings AS c ON c.show_id = b.show_id
GROUP BY a.name
ORDER BY rating DESC;
