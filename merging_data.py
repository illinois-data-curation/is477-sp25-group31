import pandas as pd

df_crash = pd.read_csv("data/chicago_crashes_cleaned.csv")
df_weather = pd.read_csv("data/chicago_weather_cleaned.csv")

df_crash["crash_date"] = pd.to_datetime(df_crash["crash_date"])
df_weather["DATE"] = pd.to_datetime(df_weather["DATE"])

df_merged = pd.merge(df_crash, df_weather, left_on="crash_date", right_on="DATE", how="left")

df_merged = df_merged.drop(columns=["DATE"])

# weather columns have NaN, we want to make it 0 so that creating visualizations is easier

numeric_cols = df_merged.select_dtypes(include=["number"]).columns
df_merged[numeric_cols] = df_merged[numeric_cols].fillna(0)

df_merged.replace('', pd.NA, inplace=True)
df_merged.fillna(0.0, inplace=True)

df_merged.drop(columns=['LATITUDE', 'LONGITUDE', 'ELEVATION'], inplace=True)

df_merged['crash_date'] = pd.to_datetime(df_merged['crash_date'])
df_merged['injuries_total'] = pd.to_numeric(df_merged['injuries_total'], errors='coerce')
df_merged = df_merged[(df_merged['latitude'] != 0.0) & (df_merged['longitude'] != 0.0)]

df_merged.to_csv("data/crash_weather_merged.csv", index=False)

print(df_merged.columns)
