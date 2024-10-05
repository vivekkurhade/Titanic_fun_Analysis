
# Titanic Data Analysis and Visualization

This project analyzes the Titanic dataset using Python, NumPy, Pandas. It focuses on examining passenger survival trends, fare statistics, and age distributions, and includes key data transformations for missing values and irrelevant columns.

## Overview

The project demonstrates how to:
- Load and clean the dataset.
- Perform basic exploratory data analysis (EDA).
- Group and aggregate data based on different attributes.
- Visualize and summarize results to identify key trends in survival rates, passenger classes, and fare distributions.

### Libraries Used
-   NumPy  : For numerical operations and array handling.
-   Pandas  : For data manipulation and analysis.

### Dataset

The analysis is based on the Titanic dataset, which contains the following columns:
-   survived  : Whether the passenger survived (1) or not (0).
-   pclass  : Passenger class (1st, 2nd, or 3rd class).
-   sex  : Gender of the passenger.
-   age  : Age of the passenger (some values are missing and are handled during preprocessing).
-   fare  : Fare paid for the ticket.
-   cabin  ,   sibsp  : Columns dropped from the dataset during analysis.

### Key Operations

1.   Data Loading  : The Titanic dataset is loaded using `pandas.read_csv()`.
2.   Missing Data Handling  :
   - The `age` column is filled with the median age where values are missing.
   - The `cabin` and `sibsp` columns are dropped for simplification.
3.   Data Grouping  :
   - Data is grouped by   pclass   to calculate the average fare paid per passenger class.
   - Gender-based survival rates are aggregated using the `groupby` function.
4.   Statistical Analysis  :
   - Calculating the mean and median for age and fare distributions.
   - Comparing the median fare for survivors vs. non-survivors.

### Output Example

- Display of the first 5 rows of the dataset.
- Shape of the dataset.
- List of female passengers.
- Grouped summary of survival rates by gender.
- Passenger class analysis based on fare.
- Median fare for survivors vs. non-survivors.

### How to Run

1. Install the necessary dependencies:
   ```bash
   pip install numpy pandas matplotlib
   ```

2. Place the Titanic dataset (`titanic.csv`) in the project directory.

3. Run the script:
   ```bash
   python titanic_analysis.py
   ```

### Results

- Analysis provides insights into how fare, age, and class affected survival rates on the Titanic.
- Data reveals that female passengers had a higher survival rate.
- First-class passengers generally paid higher fares on average compared to other classes.

