SELECT condition, COUNT(DISTINCT subject_id) AS num_subjects
FROM samples
GROUP BY condition;