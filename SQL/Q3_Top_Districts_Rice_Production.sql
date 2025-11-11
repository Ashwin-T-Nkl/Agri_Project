-- Q3. Question: Find the Top 10 Districts by Rice Production for a Selected State

SELECT 
    dist_name,
    state_name,
    SUM(rice_production) AS total_rice
FROM 
    agri_data
WHERE 
    state_name = 'Tamil Nadu'
GROUP BY 
    dist_name, state_name
ORDER BY 
    total_rice DESC
LIMIT 10;
