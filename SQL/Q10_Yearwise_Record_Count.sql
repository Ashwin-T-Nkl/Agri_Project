-- Q10. Question: Count Number of Records for Each Year

SELECT
    year,
    COUNT(*) AS rows_in_year
FROM
    agri_data
GROUP BY
    year
ORDER BY
    year;
