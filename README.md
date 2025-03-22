# Cell Count Analysis Pipeline

This Python program processes cell count data from melanoma samples, computes relative frequencies, and performs statistical analysis comparing responders vs non-responders for treatment `tr1`.

## Installation

1. Install the required dependencies:

```
pip install -r requirements.txt
```

2. Prepare your data:
   - Place the **cell-count.csv** file in the `data/` directory.

## Usage

1. Run the Python script:

```
python cell_count_analysis.py
```

2. Outputs:
   - A CSV file (`output_cell_counts.csv`) containing the relative frequencies and cell counts.
   - Boxplots comparing the relative frequencies of immune populations between responders and non-responders.
   - Statistical results (Shapiro-Wilk test, t-test/Mann-Whitney U test).

## License

This project is licensed under the MIT License.

## Answers to questions after running analysis:

2b. 
Based on the statistical tests:

Significant differences in relative frequencies between responders and non-responders were found in:
- cd4_t_cell (t-test p-value: .0008)
- monocyte (t-test p-value: .0175)
For b_cell, cd8_t_cell, and nk_cell, there were no significant differences, as their p-values were above .05.

2. 
There are many advantages to capturing this information in a database.  Databases make it easier to scale as the database expands, as alluded to in question 1.  It also makes it easier to query data efficiently and structure it in a way that is best for advanced analyses.  Data consistency and security is another advantage, especially for potentially sensitive data like this.  All in all, a database would be essential for this type of information.
