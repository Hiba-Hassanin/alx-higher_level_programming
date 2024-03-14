-- List number of records with same score in second_table in hbtn_0c_0
-- Display score and count with label "number", sorted by count (descending)

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
