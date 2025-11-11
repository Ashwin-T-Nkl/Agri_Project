-- Q1. Find the Top 10 States by Total Rice Production

SELECT 
    state_name,
    ROUND(SUM(rice_production), 2) AS total_rice
FROM 
    agri_data
GROUP BY 
    state_name
ORDER BY 
    total_rice DESC
LIMIT 10;