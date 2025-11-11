-- Q5. Question: Find Oilseeds Production by State for the Most Recent Year

SELECT 
    state_name,
    year,
    SUM(oilseeds_production) AS total_oilseeds
FROM 
    agri_data
WHERE 
    year = (SELECT MAX(year) FROM agri_data)
    AND oilseeds_production > 0
GROUP BY 
    state_name, year
ORDER BY 
    total_oilseeds DESC;
