-- List all cities with their corresponding state names from the hbtn_0d_usa database
SELECT a.`id`, a.`name`, b.`name`
  FROM `cities` AS a
       INNER JOIN `states` AS b
       ON a.`state_id` = b.`id`
 ORDER BY a.`id`;
