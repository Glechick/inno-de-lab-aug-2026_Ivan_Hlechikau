SELECT 
    sub.ShortName,
    sub.Name,
    COUNT(*) AS TotalRetakes,
    AVG(f.AttemptNumber) AS AvgAttempts
FROM fact_students_grades f
JOIN dim_subject sub ON f.Subject_sk = sub.Subject_sk
WHERE f.AttemptNumber > 1
GROUP BY sub.ShortName, sub.Name
ORDER BY TotalRetakes DESC;
