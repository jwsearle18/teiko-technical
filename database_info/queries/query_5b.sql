SELECT s.response, COUNT(s.sample_id) AS num_samples
FROM samples s
WHERE s.treatment = 'tr1'
  AND s.sample_type = 'PBMC'
  AND s.time_from_treatment_start = 0
  AND s.condition = 'melanoma'
GROUP BY s.response;