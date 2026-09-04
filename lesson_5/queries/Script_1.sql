SELECT 
    s.Course,
    AVG(f.GradeNumeric) AS AvgGrade
FROM fact_students_grades f
JOIN dim_student s ON f.Student_sk = s.Student_sk
WHERE f.LessonType = 'Экзамен' AND f.GradeNumeric IS NOT NULL
GROUP BY s.Course
ORDER BY s.Course;
