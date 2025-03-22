CREATE TABLE projects (
    project_id,
    project_name,
    project_description,
    start_date,
    end_date
);

CREATE TABLE samples (
    sample_id,
    project_id, 
    subject_id,
    sample_name,
    collection_date,
    sample_type,
    response,
    treatment,
    condition,
    age,
    sex,
    time_from_treatment_start,
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

CREATE TABLE cell_counts (
    cell_count_id,
    sample_id,
    b_cell,
    cd8_t_cell,
    cd4_t_cell,
    nk_cell,
    monocyte,
    total_count,
    FOREIGN KEY (sample_id) REFERENCES samples(sample_id)
);
