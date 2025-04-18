This project explores the prediction of future Permanent Residency (PR) admissions to Canada from historical immigration and labor market data sets. 
The goal is to allow data-informed observations of future trends in PR issuance by province and country of citizenship.
We utilized several machine learning regression techniques like Random Forest, XGBoost, and Linear Regression, ultimately stacking them with a Voting Regressor ensemble for more consistent and accurate predictions. 
The predictions are finally visualized with a Power BI dashboard for ease of interpretability and policy-level recommendations.

1. Objectives:

* Forecast PR counts by province and country of citizenship
* Identify patterns and influential features contributing to PR intake
* Enable better planning and understanding of Canada’s immigration landscape

2. Key Components

* Data Cleaning and Preprocessing: Merged and refined datasets from multiple sources
* Exploratory Data Analysis (EDA): Visualizations to understand trends and relationships

3. Model Development:

* Baseline: Linear Regression
* Tree-based models: Random Forest, XGBoost
* Final: Voting Regressor (ensemble model)
* Performance Evaluation: Metrics used include R², MAE, and RMSE
* Dashboard: Power BI dashboard for interactive visualizations

4. Tools and Libraries

* Python (Pandas, NumPy, Scikit-learn, XGBoost, Matplotlib)
* Power BI for dashboards
* Jupyter Notebook for development and visualization

5. Datasets Used

* IRCC Permanent Residents – Monthly Open Data
* Statistics Canada – GDP by Industry
* Supporting variables: gender, age, province, immigration category, country of citizenship

6. Why Ensemble Methods?
   
Ensemble models such as the Voting Regressor combine multiple algorithms to improve predictive accuracy and reduce variance. 
Compared to individual models, the ensemble approach showed more consistent and reliable performance across different prediction tasks.
