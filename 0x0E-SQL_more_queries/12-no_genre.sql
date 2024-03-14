-- List all shows without a linked genre from the hbtn_0d_tvshows database
SELECT a.title, b.genre_id
FROM hbtn_0d_tvshows.tv_shows AS a
LEFT JOIN hbtn_0d_tvshows.tv_show_genres AS b ON a.id = b.tv_show_id
WHERE b.genre_id IS NULL
ORDER BY a.title ASC, b.genre_id ASC;
