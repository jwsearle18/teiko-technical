SELECT s.sample_id, s.sample_name, s.response, s.treatment, s.sample_type, s.time_from_treatment_start, 
       c.b_cell, c.cd8_t_cell, c.cd4_t_cell, c.nk_cell, c.monocyte, c.total_count
FROM samples s
JOIN cell_counts c ON s.sample_id = c.sample_id
WHERE s.treatment = 'tr1' 
  AND s.sample_type = 'PBMC'
  AND s.time_from_treatment_start = 0
  AND s.condition = 'melanoma';