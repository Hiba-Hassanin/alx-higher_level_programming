-- List all shows and their linked genres from the hbtn_0d_tvshows database
SELECT tv_shows.title, tv_genres.name
FROM hbtn_0d_tvshows.tv_shows
LEFT JOIN hbtn_0d_tvshows.tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
LEFT JOIN hbtn_0d_tvshows.tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
