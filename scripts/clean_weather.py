import pandas as pd
import hashlib

#cleaning weather data

df = pd.read_csv("data/chicago_weather_raw_cleaned.csv")

df["DATE"] = pd.to_datetime(df["DATE"], errors="coerce")

df = df.dropna(subset=["DATE"])

keep_cols = ["DATE", "LATITUDE", "LONGITUDE"]
weather_cols = [col for col in df.columns if col not in keep_cols and df[col].dtype != "object"]

df[weather_cols] = df[weather_cols].apply(pd.to_numeric, errors="coerce")

df_weather_avg = df.groupby("DATE")[weather_cols].mean().reset_index()

df_location = df.groupby("DATE")[["LATITUDE", "LONGITUDE"]].mean().reset_index()

df_cleaned = pd.merge(df_location, df_weather_avg, on="DATE")

df_cleaned = df_cleaned.drop(columns=["WDF2", "WDF5", "WSF2", "WSF5","SNWD", "DAPR", "MDPR", "WESD", "WESF", "TMIN", "TOBS", "PGTM"], errors="ignore")
df_cleaned = df_cleaned.rename(columns={
    "WT01": "fog_or_freezing_fog",
    "WT02": "heavy_fog_or_mist",
    "WT03": "thunderstorms",
    "WT04": "ice_pellets_or_small_hail",
    "WT05": "hail_large",
    "WT06": "glaze_or_rime",
    "WT08": "smoke_or_haze",
    "WT09": "blowing_or_drifting_snow",
    "WT11": "high_or_damaging_winds",
    "AWND": "avg_wind_speed_mps",
    "PRCP": "precipitation_mm",
    "SNOW": "snowfall_mm",
    "TMAX": "max_temp_tenths_C"
})

df_cleaned["avg_temp_tenths_C"] = df_cleaned["TAVG"].fillna(df_cleaned["max_temp_tenths_C"])

df_cleaned = df_cleaned.drop(columns=["TAVG", "max_temp_tenths_C"], errors="ignore")

df_cleaned.to_csv("data/chicago_weather_cleaned.csv", index=False)

with open("data/chicago_weather_cleaned.csv", "rb") as f:
    weather_data = f.read()
    weather_sha = hashlib.sha256(weather_data).hexdigest()

with open("data/chicago_weather_cleaned.sha", "w") as f:
    f.write(weather_sha)
