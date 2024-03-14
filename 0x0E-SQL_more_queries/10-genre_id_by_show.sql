-- List all shows with at least one genre linked from the hbtn_0d_tvshows database
SELECT a.`title`, b.`genre_id`
  FROM `tv_shows` AS a
        INNER JOIN `tv_show_genres` AS b
	ON a.`id` = b.`show_id`
 ORDER BY a.`title`, b.`genre_id`;
