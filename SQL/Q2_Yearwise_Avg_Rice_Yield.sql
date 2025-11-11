-- Q2. Question: Find the Year-wise Average Rice Yield (Rounded to 2 Decimals)


SELECT 
    year,
    ROUND(AVG(rice_yield), 2) AS average_yield
FROM 
    agri_data
WHERE 
    rice_yield > 0
GROUP BY 
    year
ORDER BY 
    year;
