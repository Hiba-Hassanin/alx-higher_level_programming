-- List all genres not linked to the show Dexter from the hbtn_0d_tvshows database
SELECT DISTINCT c.name
FROM tv_genres AS c
INNER JOIN tv_show_genres AS b ON c.id = b.genre_id
INNER JOIN tv_shows AS a ON b.show_id = a.id
WHERE c.name NOT IN (
    SELECT c.name
    FROM tv_genres AS c
    INNER JOIN tv_show_genres AS b ON c.id = b.genre_id
    INNER JOIN tv_shows AS a ON b.show_id = a.id
    WHERE a.title = "Dexter"
)
ORDER BY c.name;
