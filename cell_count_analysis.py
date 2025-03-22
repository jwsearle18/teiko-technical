import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

cell_count_df = pd.read_csv('data/cell-count.csv')

# 1
population_cols = ['b_cell', 'cd8_t_cell', 'cd4_t_cell', 'nk_cell', 'monocyte']
cell_count_df['total_count'] = cell_count_df[population_cols].sum(axis=1)
cell_count_df_melted = pd.melt(cell_count_df, id_vars=['sample', 'total_count'], value_vars=population_cols, var_name='population', value_name='count')
cell_count_df_melted['percentage'] = 100*cell_count_df_melted['count']/cell_count_df_melted['total_count']
output_df = cell_count_df_melted
other_cols = [col for col in cell_count_df.columns if col not in ['sample', 'total_count'] + population_cols]
cell_count_df_melted = pd.merge(cell_count_df_melted, cell_count_df[['sample'] + other_cols], on='sample', how='left')
output_df.to_csv('output_cell_counts.csv', index=False)

# 2
filtered_cell_count_df = cell_count_df_melted[(cell_count_df_melted['treatment'] == 'tr1') & (cell_count_df_melted['sample_type'] == 'PBMC')]
responders_df = filtered_cell_count_df[filtered_cell_count_df['response'] == 'y']
non_responders_df = filtered_cell_count_df[filtered_cell_count_df['response'] == 'n']
comparison_df = pd.concat([responders_df, non_responders_df])

for population in population_cols:  
    population_data = comparison_df[comparison_df['population'] == population]  

    sns.boxplot(x='response', y='percentage', data=population_data)
    plt.title(f'{population} Relative Frequencies by Response to tr1 Treatment')
    plt.show()

    responders = population_data[population_data['response'] == 'y']
    non_responders = population_data[population_data['response'] == 'n']

    _, p_value_responder = stats.shapiro(responders['percentage'])
    _, p_value_non_responder = stats.shapiro(non_responders['percentage'])

    print(f"Normality test p-values for {population}:")
    print(f"Responder p-value: {p_value_responder}, Non-Responder p-value: {p_value_non_responder}")

    if p_value_responder > 0.05 and p_value_non_responder > 0.05:
        t_stat, p_val = stats.ttest_ind(responders['percentage'], non_responders['percentage'])
        print(f"{population} - t-test p-value: {p_val}")
    else:
        u_stat, p_val = stats.mannwhitneyu(responders['percentage'], non_responders['percentage'])
        print(f"{population} - Mann-Whitney U test p-value: {p_val}")