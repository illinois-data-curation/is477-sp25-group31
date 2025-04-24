import pandas as pd
import plotly.express as px

df = pd.read_csv("data/crash_weather_merged.csv")

df = df.dropna(subset=['latitude', 'longitude'])

fig = px.density_map(
    df,
    lat='latitude',
    lon='longitude',
    z='injuries_total',
    radius=10,
    center=dict(lat=41.8781, lon=-87.6298),  # Chicago 41.8781° N, 87.6298° W
    zoom=9,
    title="Crash Density Heatmap - Chicago"
)

fig.write_html("heatmap.html")
fig.show()
