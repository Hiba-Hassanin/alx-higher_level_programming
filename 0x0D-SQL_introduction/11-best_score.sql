-- List records with score >= 10 from second_table in hbtn_0c_0
-- Display score and name, ordered by score (top first)
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
