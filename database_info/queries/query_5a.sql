SELECT p.project_name, COUNT(s.sample_id) AS num_samples
FROM samples s
JOIN projects p ON s.project_id = p.project_id
WHERE s.treatment = 'tr1'
  AND s.sample_type = 'PBMC'
  AND s.time_from_treatment_start = 0
  AND s.condition = 'melanoma'
GROUP BY p.project_name;