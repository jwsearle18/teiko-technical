SELECT d.gender, COUNT(s.sample_id) AS num_samples
FROM samples s
JOIN demographics d ON s.sample_id = d.sample_id
WHERE s.treatment = 'tr1'
  AND s.sample_type = 'PBMC'
  AND s.time_from_treatment_start = 0
  AND s.condition = 'melanoma'
GROUP BY d.gender;