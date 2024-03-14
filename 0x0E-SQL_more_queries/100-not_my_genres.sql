-- List all genres not linked to the show Dexter from the hbtn_0d_tvshows database
SELECT name
FROM hbtn_0d_tvshows.tv_genres
WHERE id NOT IN (
    SELECT genre_id
    FROM hbtn_0d_tvshows.tv_show_genres
    WHERE tv_show_id = (
        SELECT id
        FROM hbtn_0d_tvshows.tv_shows
        WHERE title = 'Dexter'
    )
) OR id IS NULL
ORDER BY name ASC;
