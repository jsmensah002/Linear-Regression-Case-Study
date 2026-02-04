QUESTION: With a GDP per capita (USD) of 50000 and Population Density (people per sq. km of land area) of 500, predict the unemployment rate for Spain in the year 2026.

METHOD:
- Built a multivariate linear regression model to predict unemployment rate in a particular country using GDP per capita, population density, year, and country-level dummy variable.
- Compared the mean vs median imputation for missing values.
- Initially evaluated the model on the full dataset, then later implemented the 80/20 train-test split to assess the performance.

Results from the mean case study:
- Unemployment rate prediction = 11.56%
- R^2 (full dataset) = 0.41627
- R^2 (Trained 80% of the data) = 0.42121
- R^2 (Tested 20% of the data) = 0.38554

Results from the median case study:
- Unemployment rate prediction = 12.09%
- R^2 (full dataset) = 0.421394
- R^2 (Trained 80% of the data) = 0.424784
- R^2 (Tested 20% of the data)  = 0.39686


Key Insights:
From this case study, it can be concluded that replacing null values with the median has a slightly higher model performance than the mean. 



