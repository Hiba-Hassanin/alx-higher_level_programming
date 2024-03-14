-- List all shows without the genre Comedy from the hbtn_0d_tvshows database
SELECT title
FROM hbtn_0d_tvshows.tv_shows
WHERE id NOT IN (
    SELECT tv_show_id
    FROM hbtn_0d_tvshows.tv_show_genres
    WHERE genre_id = (
        SELECT id
        FROM hbtn_0d_tvshows.tv_genres
        WHERE name = 'Comedy'
    )
)
ORDER BY title ASC;
