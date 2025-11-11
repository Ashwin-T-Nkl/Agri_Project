-- Q4. Question: Show the Year-wise Maize Production Trend for a Selected State

SELECT 
    year,
    state_name,
    SUM(maize_production) AS total_maize
FROM 
    agri_data
WHERE 
    state_name = 'Tamil Nadu'   -- change the state name to get it's Maize data
GROUP BY 
    year, state_name
ORDER BY 
    year ASC;
