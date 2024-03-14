-- List all records of second_table in hbtn_0c_0
-- Display score and name, ordered by descending score
-- Exclude rows without a name value

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
