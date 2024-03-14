-- List all genres and the number of shows linked to each from the hbtn_0d_tvshows database
SELECT a.`name` AS `genre`,
       COUNT(*) AS `number_of_shows`
  FROM `tv_genres` AS a
       INNER JOIN `tv_show_genres` AS b
       ON a.`id` = b.`genre_id`
 GROUP BY a.`name`
 ORDER BY `number_of_shows` DESC;
