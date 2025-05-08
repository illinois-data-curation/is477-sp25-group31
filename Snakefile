rule all:
    input:
        "normalized_weather_crashes.png"

rule clean_crashes:
    input:
        "data/chicago_crashes.csv"
    output:
        "data/chicago_crashes_cleaned.csv"
    shell:
        "python scripts/clean_crashes.py"

rule clean_weather:
    input:
        "data/weather_conditions.csv"
    output:
        "data/chicago_weather_cleaned.csv"
    shell:
        "python scripts/clean_weather.py"

rule merge_data:
    input:
        crashes="data/chicago_crashes_cleaned.csv",
        weather="data/chicago_weather_cleaned.csv"
    output:
        "data/crash_weather_merged.csv"
    shell:
        "python scripts/merging_data.py"

rule generate_visuals:
    input:
        "data/crash_weather_merged.csv"
    output:
        "results/normalized_weather_crashes.png"
    shell:
        "python scripts/visualization.py"
