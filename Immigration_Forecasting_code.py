# Data Processing - BirthPlace of PR People
import pandas as pd
# Read the Excel file
file_path = r"C:\Users\afros\Downloads\BirthPlace_Place_PR.xlsx"
df = pd.read_excel(file_path)
# Display the first few rows
df.tail()
df_melted = df.melt(id_vars=["Country of Citizenship"], var_name="Year_Month", value_name="Value")
# Extract the last two digits of the year and convert to full year (e.g., 15 → 2015)
df_melted["Year"] = "20" + df_melted["Year_Month"].str[-2:]
# Extract the month (first three letters)
df_melted["Month"] = df_melted["Year_Month"].str[:4]
# Select relevant columns and rename 'Value' to 'Population count'
df_origin = df_melted[["Country of Citizenship", "Year", "Month", "Value"]].copy()
df_origin.rename(columns={"Value": "Population count"}, inplace=True)
# Check the cleaned dataframe
print(df_origin.head())
# Define the mapping from short month names to full month names
month_mapping = {
    'Jaan': 'January',
    'Feeb': 'February',
    'Maar': 'March',
    'Aprr': 'April',
    'Maay': 'May',
    'Juun': 'June',
    'Juul': 'July',
    'Auug': 'August',
    'Seep': 'September',
    'Occt': 'October',
    'Noov': 'November',
    'Deec': 'December'
}

# Replace the short month names in the 'Month' column with full month names
df_origin['Month'] = df_origin['Month'].map(month_mapping)
df_origin
df_origin.to_excel('BirthPlace_PR_People_ML.xlsx', index=False)
# Data Processing - Gender of PR People
import pandas as pd
# Read the Excel file
file_path = r"C:\Users\afros\Downloads\Gender_pr.csv"
df = pd.read_csv(file_path)
# Display the first few rows
df.head()
df_melted = df.melt(id_vars=["Gender"], var_name="Year_Month", value_name="Value")
df_melted
df_melted["Year_Month"].unique()
# Extract the last two digits of the year and convert to full year (e.g., 15 → 2015)
df_melted["Year"] = "20" + df_melted["Year_Month"].str[-2:]
# Extract the month (first three letters)
df_melted["Month"] = df_melted["Year_Month"].str[:4]
# Select relevant columns and rename 'Value' to 'Population count'
df_origin = df_melted[["Gender", "Year", "Month", "Value"]].copy()
df_origin.rename(columns={"Value": "Population count"}, inplace=True)
# Check the cleaned dataframe
print(df_origin.head())
distinct_months = df_origin["Month"].unique()
distinct_months
# Define the mapping from short month names to full month names
month_mapping = {
    'Jaan': 'January',
    'Feeb': 'February',
    'Maar': 'March',
    'Aprr': 'April',
    'Maay': 'May',
    'Juun': 'June',
    'Juul': 'July',
    'Auug': 'August',
    'Seep': 'September',
    'Occt': 'October',
    'Noov': 'November',
    'Deec': 'December'
}

# Replace the short month names in the 'Month' column with full month names
df_origin['Month'] = df_origin['Month'].map(month_mapping)
df_origin
# Convert 'Population count' to numeric, handling non-numeric values
df_origin["Population count"] = pd.to_numeric(df_origin["Population count"], errors='coerce').fillna(0)
# Group by Gender, Year, Month and sum the Population count
df_grouped = df_origin.groupby(["Gender", "Year", "Month"], as_index=False)["Population count"].sum()
df_grouped["Population count"] = df_grouped["Population count"].astype(int)
print(df_grouped)
df_grouped.to_excel('Gender_PR_People.xlsx', index=False)
# Data Processing - Age Category PR
import pandas as pd
# Read the Excel file
file_path = r"C:\Users\afros\Downloads\Agecategory_Pr.xlsx"
df = pd.read_excel(file_path)
# Display the first few rows
df.tail()
df_melted = df.melt(id_vars=["Province/Territory", "Age Group"], var_name="Year_Month", value_name="Value")
df_melted
# Extract the last two digits of the year and convert to full year (e.g., 15 → 2015)
df_melted["Year"] = "20" + df_melted["Year_Month"].str[-2:]
# Extract the month (first three letters)
df_melted["Month"] = df_melted["Year_Month"].str[:4]
# Select relevant columns and rename 'Value' to 'Population count'
df_origin = df_melted[["Province/Territory","Age Group", "Year", "Month", "Value"]].copy()
df_origin.rename(columns={"Value": "Population count"}, inplace=True)
# Check the cleaned dataframe
print(df_origin.head())
# Define the mapping from short month names to full month names
month_mapping = {
    'Jaan': 'January',
    'Feeb': 'February',
    'Maar': 'March',
    'Aprr': 'April',
    'Maay': 'May',
    'Juun': 'June',
    'Juul': 'July',
    'Auug': 'August',
    'Seep': 'September',
    'Occt': 'October',
    'Noov': 'November',
    'Deec': 'December'
}

# Replace the short month names in the 'Month' column with full month names
df_origin['Month'] = df_origin['Month'].map(month_mapping)
df_origin
df_origin.to_excel('AgeCategory_PR_People.xlsx', index=False)
# Data Processing - Job Category PR
import pandas as pd
# Read the Excel file
file_path = r"C:\Users\afros\Downloads\Occupation_PR.xlsx"
df = pd.read_excel(file_path)  # Use read_excel instead of read_csv
# Display the first few rows
df.tail()
job_categories
# Function to categorize occupations
def categorize_occupation(occupation):
    for category, codes in job_categories.items():
        for code in codes:
            if occupation.startswith(code.split(" - ")[0]):
                return category
    return "Other"
df["Job Category"] = df["Intended Occupation"].astype(str).apply(categorize_occupation)
df = df.drop(columns=["Intended Occupation"])
df.head()
df_melted = df.melt(id_vars=["Job Category"], var_name="Year_Month", value_name="Value")
# Extract the last two digits of the year and convert to full year (e.g., 15 → 2015)
df_melted["Year"] = "20" + df_melted["Year_Month"].str[-2:]
# Extract the month (first three letters)
df_melted["Month"] = df_melted["Year_Month"].str[:4]
# Select relevant columns and rename 'Value' to 'Population count'
df_origin = df_melted[["Job Category", "Year", "Month", "Value"]].copy()
df_origin.rename(columns={"Value": "Population count"}, inplace=True)
# Check the cleaned dataframe
print(df_origin.head())
# Define the mapping from short month names to full month names
month_mapping = {
    'Jaan': 'January',
    'Feeb': 'February',
    'Maar': 'March',
    'Aprr': 'April',
    'Maay': 'May',
    'Juun': 'June',
    'Juul': 'July',
    'Auug': 'August',
    'Seep': 'September',
    'Occt': 'October',
    'Noov': 'November',
    'Deec': 'December'
}

# Replace the short month names in the 'Month' column with full month names
df_origin['Month'] = df_origin['Month'].map(month_mapping)
df_origin
df_origin["Population count"] = pd.to_numeric(df_origin["Population count"], errors='coerce').fillna(0)
# Group by Gender, Year, Month and sum the Population count
df_grouped = df_origin.groupby(["Job Category", "Year", "Month"], as_index=False)["Population count"].sum()
df_grouped["Population count"] = df_grouped["Population count"].astype(int)
df_grouped.head()
df_origin.to_excel('JobCategory_PR_People.xlsx', index=False)
# Data Processing - Metropolitan Category PR
import pandas as pd
# Read the Excel file
file_path = r"C:\Users\afros\Downloads\Metropolitan_PR_Category.xlsx"
df = pd.read_excel(file_path)
# Display the first few rows
df.tail()
print("Available columns:", df.columns)
df_melted = df.melt(id_vars=[" Province/Territory","Metropolitan Area"], var_name="Year_Month", value_name="Value")
# Extract the last two digits of the year and convert to full year (e.g., 15 → 2015)
df_melted["Year"] = "20" + df_melted["Year_Month"].str[-2:]
# Extract the month (first three letters)
df_melted["Month"] = df_melted["Year_Month"].str[:4]
# Select relevant columns and rename 'Value' to 'Population count'
df_origin = df_melted[[" Province/Territory","Metropolitan Area", "Year", "Month", "Value"]].copy()
df_origin.rename(columns={"Value": "Population count"}, inplace=True)
# Check the cleaned dataframe
print(df_origin.head())
# Define the mapping from short month names to full month names
month_mapping = {
    'Jaan': 'January',
    'Feeb': 'February',
    'Maar': 'March',
    'Aprr': 'April',
    'Maay': 'May',
    'Juun': 'June',
    'Juul': 'July',
    'Auug': 'August',
    'Seep': 'September',
    'Occt': 'October',
    'Noov': 'November',
    'Deec': 'December'
}

# Replace the short month names in the 'Month' column with full month names
df_origin['Month'] = df_origin['Month'].map(month_mapping)
df_origin
df_origin.to_excel('Metropolitant_PR_People.xlsx', index=False)
# Data Processing - Immigration Category PR
import pandas as pd
# Read the Excel file
file_path = r"C:\Users\afros\Downloads\Immigration_status_PR.xlsx"
df = pd.read_excel(file_path)
# Display the first few rows
df.tail()
print("Available columns:", df.columns)
df_melted = df.melt(id_vars=["Province/Territory ","Immigration Category"], var_name="Year_Month", value_name="Value")
# Extract the last two digits of the year and convert to full year (e.g., 15 → 2015)
df_melted["Year"] = "20" + df_melted["Year_Month"].str[-2:]
# Extract the month (first three letters)
df_melted["Month"] = df_melted["Year_Month"].str[:4]
# Select relevant columns and rename 'Value' to 'Population count'
df_origin = df_melted[["Province/Territory ","Immigration Category", "Year", "Month", "Value"]].copy()
df_origin.rename(columns={"Value": "Population count"}, inplace=True)
# Check the cleaned dataframe
print(df_origin.head())
# Define the mapping from short month names to full month names
month_mapping = {
    'Jaan': 'January',
    'Feeb': 'February',
    'Maar': 'March',
    'Aprr': 'April',
    'Maay': 'May',
    'Juun': 'June',
    'Juul': 'July',
    'Auug': 'August',
    'Seep': 'September',
    'Occt': 'October',
    'Noov': 'November',
    'Deec': 'December'
}

# Replace the short month names in the 'Month' column with full month names
df_origin['Month'] = df_origin['Month'].map(month_mapping)
df_origin
df_origin.to_excel('Immigrationstatus_PR_People.xlsx', index=False)
# Modeling And Visulization
# Ensemble PR Predictions for 2025 + Visualization
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
# === 1. Load and Clean Data ===
df = pd.read_excel(r"C:\Users\afros\Documents\Final Semester Project\Metropolitant_PR_People.xlsx")
df.columns = df.columns.str.strip()
month_map = {month: i+1 for i, month in enumerate(["January", "February", "March", "April", "May", "June",
                                                   "July", "August", "September", "October", "November", "December"])}
df["Month"] = df["Month"].map(month_map)
df = df.rename(columns={"Province/Territory": "Province", "Metropolitan Area": "Metro", "Population count": "PR_Population"})
df = df.dropna(subset=["Province", "Metro", "Year", "Month", "PR_Population"])

# === 2. Preprocessing ===
X = df[df["Year"] <= 2024][["Province", "Metro", "Year", "Month"]]
y = df[df["Year"] <= 2024]["PR_Population"]

preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), ["Province", "Metro"])
], remainder="passthrough")
# === 3. Model Tuning ===
# Random Forest
rf_pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(random_state=42))
])
rf_params = {"regressor__n_estimators": [50, 100], "regressor__max_depth": [None, 10]}
rf_search = GridSearchCV(rf_pipeline, rf_params, cv=3, scoring='neg_mean_squared_error', n_jobs=-1)
rf_search.fit(X, y)
best_rf_model = rf_search.best_estimator_

# Gradient Boosting
gb_pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", GradientBoostingRegressor(random_state=42))
])
gb_params = {"regressor__n_estimators": [100, 200], "regressor__learning_rate": [0.05, 0.1], "regressor__max_depth": [3, 5]}
gb_search = GridSearchCV(gb_pipeline, gb_params, cv=3, scoring='neg_mean_squared_error', n_jobs=-1)
gb_search.fit(X, y)
best_gb_model = gb_search.best_estimator_

# Linear Regression (no tuning)
lr_model = Pipeline([("preprocessor", preprocessor), ("regressor", LinearRegression())])
lr_model.fit(X, y)

# === 4. Prediction Dataset ===
years_full = list(range(2018, 2028))
months = list(range(1, 13))
locations = df[["Province", "Metro"]].drop_duplicates()
predict_df = pd.DataFrame([
    {"Province": row["Province"], "Metro": row["Metro"], "Year": year, "Month": month}
    for _, row in locations.iterrows()
    for year in years_full
    for month in months
])

# === 5. Predict ===
predict_df["LR_Pred"] = lr_model.predict(predict_df)
predict_df["RF_Pred"] = best_rf_model.predict(predict_df)
predict_df["GB_Pred"] = best_gb_model.predict(predict_df)
predict_df["Ensemble_Pred"] = predict_df[["LR_Pred", "RF_Pred", "GB_Pred"]].mean(axis=1)

# Aggregate by year and metro
yearly_trend = predict_df.groupby(["Year", "Province", "Metro"])["Ensemble_Pred"].sum().reset_index()
yearly_trend["Predicted_PR_Count"] = yearly_trend["Ensemble_Pred"].round().astype(int)

# === 6. Export Full Dataset ===
yearly_trend.to_csv("PR_Prediction_AllProvinces_2018_to_2027.csv", index=False)
print("Exported to PR_Prediction_AllProvinces_2018_to_2027.csv")

# === 7. Line Chart: Top 5 Metros ===
top5_metros = yearly_trend[yearly_trend["Year"] == 2025].nlargest(5, "Predicted_PR_Count")[["Province", "Metro"]]
trend_top5 = yearly_trend.merge(top5_metros, on=["Province", "Metro"])

plt.figure(figsize=(12, 6))
for metro in trend_top5["Metro"].unique():
    data = trend_top5[trend_top5["Metro"] == metro]
    plt.plot(data["Year"], data["Predicted_PR_Count"], label=metro)
plt.title("PR Population Trends (2018–2027) - Top 5 Metros")
plt.xlabel("Year")
plt.ylabel("Predicted PR Population")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# === 8. Bar Chart: Top 10 in 2025 ===
top10_2025 = yearly_trend[yearly_trend["Year"] == 2025].nlargest(10, "Predicted_PR_Count")
plt.figure(figsize=(12, 6))
bars = plt.barh(top10_2025["Metro"], top10_2025["Predicted_PR_Count"])
plt.xlabel("Predicted PR Count (2025)")
plt.title("Top 10 Metro Areas for PR Population in 2025 (Tuned Ensemble)")
plt.gca().invert_yaxis()
for bar in bars:
    width = bar.get_width()
    plt.text(width + 1000, bar.get_y() + bar.get_height() / 2, f"{int(width):,}", va="center")
plt.tight_layout()
plt.show()

# PR Approval efficiency based on country of citizen
import pandas as pd
import matplotlib.pyplot as plt

# === 1. Load the Cleaned/Extrapolated Data ===
df = pd.read_csv(r"C:\Users\afros\Documents\Final Semester Project\PR_Requested_vs_Approved_Extrapolated.csv")
df.columns = df.columns.str.strip()

# === 2. Aggregate by Country-Year ===
df_yearly = df.groupby(["Country", "Year"], as_index=False).agg({
    "PR_Requested": "sum",
    "PR_Approved": "sum"
})

# === 3. Total PR_Requested per Country ===
country_totals = df_yearly.groupby("Country")["PR_Requested"].sum().reset_index()

# === 4. Filter Countries with PR Requested > 8000 ===
valid_countries = country_totals[country_totals["PR_Requested"] > 8000]["Country"]
df_filtered = df_yearly[df_yearly["Country"].isin(valid_countries)]

# === 5. Re-Aggregate Total PR Stats per Country ===
summary_df = df_filtered.groupby("Country", as_index=False).agg({
    "PR_Requested": "sum",
    "PR_Approved": "sum"
})

# === 6. Calculate Approval Rate ===
summary_df["Approval_Rate"] = summary_df["PR_Approved"] / summary_df["PR_Requested"]

# === 7. Sort by PR Requested DESC ===
summary_sorted = summary_df.sort_values(by="PR_Requested", ascending=False).reset_index(drop=True)

# === 8. Plot: Top 7 Countries ===
top7 = summary_sorted.head(7)
countries = top7["Country"]
pr_requested = top7["PR_Requested"]
approval_rate = top7["Approval_Rate"] * 100  # Convert to percentage

fig, ax1 = plt.subplots(figsize=(12, 6))

# Bar chart for PR Requested
bars = ax1.bar(countries, pr_requested, color='skyblue', label='PR Requested')
ax1.set_xlabel('Country')
ax1.set_ylabel('PR Requested', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax1.set_xticklabels(countries, rotation=45, ha='right')

# Line chart for Approval Rate (%)
ax2 = ax1.twinx()
ax2.plot(countries, approval_rate, color='green', marker='o', label='Approval Rate (%)')
ax2.set_ylabel('Approval Rate (%)', color='green')
ax2.tick_params(axis='y', labelcolor='green')

# Combine legends
lines_labels = [ax.get_legend_handles_labels() for ax in [ax1, ax2]]
lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
ax1.legend(lines, labels, loc='upper left')

plt.title('Top 7 Countries by PR Requested with Approval Rate (Extrapolated Data)')
plt.tight_layout()
plt.show()

# === 9. Final Table Output ===
print("\n Final Adjusted PR Stats:")
print(summary_sorted.head(20).to_string(index=False))
summary_sorted.to_csv("Final_Country_PR_Stats_Extrapolated.csv", index=False)

# Forecasting for 2025,2026 based on citizen of country
import pandas as pd
import numpy as np
from prophet import Prophet
from pmdarima import auto_arima
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import warnings
warnings.filterwarnings("ignore")

# === 1. Load Data ===
df = pd.read_csv("PR_Requested_vs_Approved_Extrapolated.csv")
df.columns = df.columns.str.strip()

# === 2. Convert Month to Datetime ===
month_map = {
    "January": 1, "February": 2, "March": 3, "April": 4,
    "May": 5, "June": 6, "July": 7, "August": 8,
    "September": 9, "October": 10, "November": 11, "December": 12
}
df["Month_Num"] = df["Month"].map(month_map)
df["Date"] = pd.to_datetime(df["Year"].astype(str) + "-" + df["Month_Num"].astype(str) + "-01")

# === 3. Future Dates to Forecast (2025-2026) ===
future_dates = pd.date_range("2025-01-01", "2026-12-01", freq="MS")

# === 4. Forecasting Function ===
def forecast_country(data):
    data = data[["Date", "PR_Approved"]].dropna()
    data = data.set_index("Date").resample("MS").sum()
    data = data.asfreq("MS").fillna(0)

    # Prophet
    prophet_df = data.reset_index().rename(columns={"Date": "ds", "PR_Approved": "y"})
    prophet_model = Prophet(yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False)
    prophet_model.fit(prophet_df)
    future = pd.DataFrame({"ds": future_dates})
    prophet_forecast = prophet_model.predict(future)["yhat"].values

    # ARIMA
    arima_model = auto_arima(data["PR_Approved"], seasonal=False, suppress_warnings=True)
    arima_forecast = arima_model.predict(n_periods=24)

    # Holt-Winters
    hw_model = ExponentialSmoothing(data["PR_Approved"], trend="add", seasonal="add", seasonal_periods=12)
    hw_fit = hw_model.fit()
    hw_forecast = hw_fit.forecast(24)

    # SARIMA
    sarima_model = auto_arima(data["PR_Approved"], seasonal=True, m=12, suppress_warnings=True)
    sarima_forecast = sarima_model.predict(n_periods=24)

    # Ensemble
    ensemble = (prophet_forecast + arima_forecast + hw_forecast + sarima_forecast) / 4

    forecast_df = pd.DataFrame({
        "Date": future_dates,
        "Forecasted_PR_Approved": np.maximum(0, ensemble).round().astype(int)
    })

    return forecast_df

# === 5. Forecast for All Countries ===
results = []
unique_countries = df["Country"].dropna().unique()

for country in unique_countries:
    try:
        country_data = df[df["Country"] == country].copy()
        forecast_df = forecast_country(country_data)
        forecast_df["Country"] = country
        results.append(forecast_df)
        print(f"Done: {country}")
    except Exception as e:
        print(f"Skipped {country}: {e}")

# === 6. Combine All Forecasts ===
final_forecast = pd.concat(results, ignore_index=True)

# === 7. Export to CSV ===
final_forecast.to_csv("All_Countries_Ensembled_Monthly_PR_Approved_Forecast_2025_2026.csv", index=False)

# === 8. Display Sample Output ===
print("\nForecast saved as: All_Countries_Ensembled_Monthly_PR_Approved_Forecast_2025_2026.csv")
print(final_forecast.head(10))

# === 7.1 Prepare Historical Data (Monthly PR_Approved)
historical = df[["Country", "Date", "PR_Approved"]].dropna()
historical = historical.rename(columns={"PR_Approved": "Approved_Value"})
historical["Source"] = "Actual"

# === 7.2 Prepare Forecasted Data
forecast_output = final_forecast.rename(columns={"Forecasted_PR_Approved": "Approved_Value"})
forecast_output["Source"] = "Forecast"

# === 7.3 Combine Both
combined_df = pd.concat([historical, forecast_output], ignore_index=True)

# === 7.4 Sort and Save
combined_df = combined_df.sort_values(by=["Country", "Date"])
combined_df.to_csv("Combined_Actual_and_Forecast_PR_Approved_2025_2026.csv", index=False)

# === 8. Display Sample Output
print("\nForecast + Raw data saved as: Combined_Actual_and_Forecast_PR_Approved_2025_2026.csv")
print(combined_df.head(10))

import matplotlib.pyplot as plt

# --- Step 1: Top 5 Countries by PR_Requested (before 2025)
top5_requested = (
    df[df["Year"] < 2025]
    .groupby("Country")["PR_Requested"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .index.tolist()
)

# --- Step 2: Actual 2024 data (only top 5 countries)
actual_2024 = df[(df["Year"] == 2024) & (df["Country"].isin(top5_requested))]

# --- Step 3: Forecast data for top 5
forecast_top5 = final_forecast[final_forecast["Country"].isin(top5_requested)]

# --- Step 4: Plot
plt.figure(figsize=(14, 6))

# Actual 2024 (solid lines)
for country in actual_2024["Country"].unique():
    country_data = actual_2024[actual_2024["Country"] == country]
    plt.plot(country_data["Date"], country_data["PR_Approved"],
             label=f"{country} (Actual 2024)", linewidth=2)

# Forecast 2025–2026 (dashed lines)
for country in forecast_top5["Country"].unique():
    country_data = forecast_top5[forecast_top5["Country"] == country]
    plt.plot(country_data["Date"], country_data["Forecasted_PR_Approved"],
             linestyle="--", marker='o', label=f"{country} (Forecast)")

plt.title("Actual (2024) vs Forecasted (2025–2026) – Top 5 Countries by PR Requested")
plt.xlabel("Year_Month")
plt.ylabel("PR Approved")
plt.legend(title="Legend", loc="upper left", bbox_to_anchor=(1.02, 1))
plt.grid(True)
plt.tight_layout()
plt.show()

# Analysis for Age category with Province

import pandas as pd
import matplotlib.pyplot as plt

# === 1. Load Data ===
df = pd.read_excel(r"C:\Users\afros\Documents\Final Semester Project\AgeCategory_PR_People.xlsx")
df.columns = df.columns.str.strip()

# === 2. Rename columns for easier access ===
df.rename(columns={
    "Province/Territory": "Province",
    "Age Group": "Age_Group",
    "Population count": "PR_Count"
}, inplace=True)

# === 3. Aggregate yearly PR count by age group ===
yearly_age_trend = df.groupby(["Year", "Age_Group"])["PR_Count"].sum().reset_index()

# === 4. Pivot for line chart ===
pivot_data = yearly_age_trend.pivot(index="Year", columns="Age_Group", values="PR_Count").fillna(0)


# === Display the DataFrame ===
print("\n PR Approved by Age Group (Yearly):\n")
print(pivot_data.reset_index())

# === 5. Plotting ===
plt.figure(figsize=(14, 6))
pivot_data.plot(marker='o', linewidth=2, figsize=(14, 6))

plt.title("PR Approved Trend by Age Group (Yearly)")
plt.xlabel("Year")
plt.ylabel("Total PR Approved")
plt.grid(True)
plt.legend(title="Age Group", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# === Load the Data ===
df = pd.read_excel(r"C:\Users\afros\Documents\Final Semester Project\AgeCategory_PR_People.xlsx")
df.columns = df.columns.str.strip()

# === Rename columns for clarity ===
df.rename(columns={
    "Province/Territory": "Province",
    "Age Group": "Age_Group",
    "Population count": "PR_Count"
}, inplace=True)

# === Aggregate PR count by Province and Age Group ===
province_age = df.groupby(["Province", "Age_Group"])["PR_Count"].sum().reset_index()

# === Pivot to get Age Groups as columns ===
province_pivot = province_age.pivot(index="Province", columns="Age_Group", values="PR_Count").fillna(0)

# === Normalize to get % share per province ===
province_pct = province_pivot.div(province_pivot.sum(axis=1), axis=0) * 100

# === Plot the Stacked Bar Chart ===
plt.figure(figsize=(14, 6))
province_pct.plot(kind="bar", stacked=True, figsize=(14, 6), colormap="tab20")

plt.title("Age Group Share of PR Approvals by Province")
plt.ylabel("Percentage Share")
plt.xlabel("Province")
plt.legend(title="Age Group", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.show()

# === Display the Percent Share DataFrame ===
print("\n Age Group Share of PR Approvals by Province (%):\n")
print(province_pct.round(2).reset_index())

# Identify "youth-friendly" provinces — where 15–29 year olds make up >35% of all PR approvals.
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report
import numpy as np

# === 1. Load Data ===
df = pd.read_excel(r"C:\Users\afros\Documents\Final Semester Project\AgeCategory_PR_People.xlsx")
df.columns = df.columns.str.strip()

# === 2. Rename Columns ===
df.rename(columns={
    "Province/Territory": "Province",
    "Age Group": "Age_Group",
    "Population count": "PR_Count"
}, inplace=True)

# === 3. Aggregate Total PRs by Province and Age Group ===
agg_df = df.groupby(["Province", "Age_Group"])["PR_Count"].sum().reset_index()

# === 4. Pivot to get age group columns
pivot_df = agg_df.pivot(index="Province", columns="Age_Group", values="PR_Count").fillna(0)

# === 5. Feature Engineering: Convert to % share
feature_df = pivot_df.div(pivot_df.sum(axis=1), axis=0) * 100
feature_df = feature_df.reset_index()

# === 6. Create Target Column: Youth-Friendly if 15–29 age group > 35%
feature_df["Youth_Friendly"] = (feature_df["15 to 29 years old"] > 35).astype(int)

# === 7. Prepare Data
X = feature_df.drop(columns=["Province", "Youth_Friendly"])
y = feature_df["Youth_Friendly"]

# === 8. Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# === 9. Random Forest with Hyperparameter Tuning
param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [3, 5, 10, None],
    "min_samples_split": [2, 5, 10]
}

grid = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=3, scoring='accuracy')
grid.fit(X_train, y_train)

best_model = grid.best_estimator_
y_pred = best_model.predict(X_test)
y_proba = best_model.predict_proba(X_test)[:, 1]  # probability of class 1

# === 10. Final Output Table
output_df = X_test.copy()
output_df["Predicted_Label"] = y_pred
output_df["Youth_Friendly_Prob"] = np.round(y_proba, 2)
output_df["Province"] = feature_df["Province"].iloc[X_test.index].values
output_df["True_Label"] = y_test.values
output_df = output_df[["Province", "True_Label", "Predicted_Label", "Youth_Friendly_Prob"]]

# === 11. Show Output
print("\n Youth-Friendly Province Prediction Results:\n")
print(output_df.sort_values(by="Youth_Friendly_Prob", ascending=False).reset_index(drop=True))

# === 12. Classification Report
print("\n Model Performance:\n")
print(classification_report(y_test, y_pred))
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

# === 1. Load Your GeoJSON File ===
geo_df = gpd.read_file(r"C:\Users\afros\Documents\Final Semester Project\canada.geojson")  # Use a full Canada provinces shapefile

# === 2. Clean GeoDataFrame ===
geo_df["name"] = geo_df["name"].str.strip()

# === 3. Prepare Prediction DataFrame from your output_df
# Assuming you already have this:
# output_df = pd.DataFrame with columns: Province, Youth_Friendly_Prob

# Optional: Standardize province names if needed
province_clean_map = {
    "Newfoundland and Labrador Total": "Newfoundland and Labrador",
    "Northwest Territories Total": "Northwest Territories",
    "Prince Edward Island Total": "Prince Edward Island",
    "Nova Scotia Total": "Nova Scotia",
    "British Columbia Total": "British Columbia",
    "Saskatchewan Total": "Saskatchewan",
    "New Brunswick Total": "New Brunswick",
    "Manitoba Total": "Manitoba",
    "Yukon Total": "Yukon",
    "Nunavut Total": "Nunavut",
    "Alberta Total": "Alberta",
    "Ontario Total": "Ontario",
    "Quebec Total": "Quebec"
}

# Replace if output_df has "Province" ending in ' Total'
output_df["Clean_Province"] = output_df["Province"].replace(province_clean_map)

# === 4. Merge shapefile with predictions ===
merged = geo_df.merge(output_df, left_on="name", right_on="Clean_Province", how="left")

# === 5. Fill NA with 0 for clean color scaling
merged["Youth_Friendly_Prob"] = merged["Youth_Friendly_Prob"].fillna(0)
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
# === Plotting with Province Labels ===
fig, ax = plt.subplots(1, 1, figsize=(14, 8))

# Plot the choropleth
merged.plot(column="Youth_Friendly_Prob",
            cmap="YlGn", linewidth=0.8, ax=ax, edgecolor="black",
            legend=True,
            legend_kwds={"label": "Youth-Friendly Score (0–1)", "shrink": 0.5})

# Add province names at the centroid of each polygon
for idx, row in merged.iterrows():
    if row['geometry'].centroid.is_empty:
        continue
    x, y = row['geometry'].centroid.coords[0]
    province_name = row['name']
    ax.text(x, y, province_name, fontsize=8, ha='center', va='center', color="black")

# Title and formatting
ax.set_title("Youth-Friendly Provinces in Canada (with Labels)", fontsize=16)
ax.axis("off")
plt.tight_layout()
plt.show()
# Yearly PR Approvals By Immigration Category
import pandas as pd
import matplotlib.pyplot as plt
# === 1. Load Data ===
df = pd.read_excel(r"C:\Users\afros\Documents\Final Semester Project\Immigrationstatus_PR_People.xlsx")
df.columns = df.columns.str.strip()
# === 2. Rename Columns for Clarity ===
df = df.rename(columns={
    "Province/Territory": "Province",
    "Immigration Category": "Immigration_Category",
    "Population count": "PR_Count"
})
# === 3. Group by Year and Immigration Category ===
yearly_trend = df.groupby(["Year", "Immigration_Category"], as_index=False)["PR_Count"].sum()

# === 4. Pivot to Create Trend Table ===
pivot_trend = yearly_trend.pivot(index="Year", columns="Immigration_Category", values="PR_Count").fillna(0)
import matplotlib.pyplot as plt

# Plot the trend line chart with improved formatting
plt.figure(figsize=(14, 7))
ax = pivot_trend.plot(marker='o', linewidth=2, figsize=(14, 7))

# Titles and labels
plt.title(" Yearly PR Approvals by Immigration Category (2015–2024)", fontsize=16)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Total PR Approvals", fontsize=12)

# Grid and formatting
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(pivot_trend.index, rotation=45)
plt.yticks(fontsize=10)

# Legend outside the plot
plt.legend(title="Immigration Category", bbox_to_anchor=(1.02, 1), loc="upper left", fontsize=10, title_fontsize=12)

# Tight layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()
#Visualizations
import matplotlib.pyplot as plt
import seaborn as sns

# Re-importing necessary libraries for consistent output
import pandas as pd
import numpy as np
import plotly.express as px

# Regenerate all plots for export
def create_all_figures():
    figures = []

    # 1. Yearly PR Prediction by Province
    plt.figure(figsize=(14, 8))
    for province in pr_yearly['Province'].unique():
        subset = pr_yearly[pr_yearly['Province'] == province]
        plt.plot(subset['Year'], subset['Predicted_PR_Count'], label=province)
    plt.title("Yearly Predicted PR Approvals by Province (2018–2027)")
    plt.xlabel("Year")
    plt.ylabel("Predicted PR Count")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.grid(True)
    fig1 = plt.gcf()
    figures.append(("Yearly PR Predictions by Province", fig1))
    plt.close()

    # 2. Top and Bottom 10 Countries by PR Approval Rate
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top_approval, x="Approval_Rate", y="Country", palette="Greens_d")
    plt.title("Top 10 Countries by PR Approval Rate")
    plt.xlabel("Approval Rate")
    plt.ylabel("Country")
    plt.xlim(0, 1)
    plt.grid(True)
    fig2 = plt.gcf()
    figures.append(("Top 10 Countries by PR Approval Rate", fig2))
    plt.close()

    plt.figure(figsize=(10, 6))
    sns.barplot(data=bottom_approval, x="Approval_Rate", y="Country", palette="Reds_d")
    plt.title("Bottom 10 Countries by PR Approval Rate")
    plt.xlabel("Approval Rate")
    plt.ylabel("Country")
    plt.xlim(0, 1)
    plt.grid(True)
    fig3 = plt.gcf()
    figures.append(("Bottom 10 Countries by PR Approval Rate", fig3))
    plt.close()

    # 3. Forecasted PR Approvals by Country - 2025
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top_forecast_2025, x="Approved_Value", y="Country", palette="Blues_d")
    plt.title("Top 10 Countries Forecasted for PR Approvals in 2025")
    plt.xlabel("Forecasted PR Approvals")
    plt.ylabel("Country")
    plt.grid(True)
    fig4 = plt.gcf()
    figures.append(("Forecasted PR Approvals in 2025", fig4))
    plt.close()

    # 4. Forecasted PR Approvals by Country - 2026
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top_forecast_2026, x="Approved_Value", y="Country", palette="Purples_d")
    plt.title("Top 10 Countries Forecasted for PR Approvals in 2026")
    plt.xlabel("Forecasted PR Approvals")
    plt.ylabel("Country")
    plt.grid(True)
    fig5 = plt.gcf()
    figures.append(("Forecasted PR Approvals in 2026", fig5))
    plt.close()

    # 5. PR Trends by Immigration Category
    plt.figure(figsize=(14, 8))
    category_pivot.plot(kind='line', marker='o', figsize=(14, 8))
    plt.title("Yearly PR Approvals by Immigration Category")
    plt.xlabel("Year")
    plt.ylabel("PR Approval Count")
    plt.grid(True)
    plt.legend(title="Immigration Category", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    fig6 = plt.gcf()
    figures.append(("PR Approvals by Immigration Category", fig6))
    plt.close()

    return figures

# Generate all plots
all_figures = create_all_figures()

# Save figures for inclusion in the Word report
import os

output_dir = "/mnt/data/final_project_figures"
os.makedirs(output_dir, exist_ok=True)

image_paths = []
for idx, (title, fig) in enumerate(all_figures, 1):
    path = os.path.join(output_dir, f"figure_{idx}.png")
    fig.savefig(path)
    image_paths.append((title, path))

image_paths

