import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/crash_weather_merged.csv")

df['crash_date'] = pd.to_datetime(df['crash_date'])

grouped = df.groupby(['crash_date', 'weather_condition']).size().reset_index(name='daily_crashes')
avg_crashes = grouped.groupby('weather_condition')['daily_crashes'].mean().sort_values(ascending=False).reset_index()
plt.figure(figsize=(12, 6))
sns.barplot(data=avg_crashes, x='weather_condition', y='daily_crashes', palette='mako')
plt.xticks(rotation=45)
plt.title('Average Crashes per Day by Weather Condition (Jan–Apr 2025)')
plt.xlabel('Weather Condition')
plt.ylabel('Avg. Crashes per Day')
plt.tight_layout()
plt.savefig("results/normalized_weather_crashes.png")
plt.close()