-- List all genres of the show Dexter from the hbtn_0d_tvshows database
SELECT b.name
FROM hbtn_0d_tvshows.tv_shows AS a
JOIN hbtn_0d_tvshows.tv_show_genres AS c ON a.id = c.tv_show_id
JOIN hbtn_0d_tvshows.tv_genres AS b ON c.genre_id = b.id
WHERE a.title = 'Dexter'
ORDER BY b.name ASC;
