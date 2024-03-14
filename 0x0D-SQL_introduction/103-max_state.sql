-- Display max temperature of each state ordered by state name

SELECT state, MAX(temperature) AS max_temp
FROM table_name
GROUP BY state
ORDER BY state;
