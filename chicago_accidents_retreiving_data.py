import requests
import json
import pandas as pd
import hashlib

with open("chicago_api.txt") as f:
    apikey = f.readline().strip()
url = "https://data.cityofchicago.org/resource/85ca-t3if.json"

headers = {
    "X-App-Token": apikey
}

start_date = "2025-01-01T00:00:00"
end_date = "2025-04-20T23:59:59"

offset = 0
limit = 50000
all_data = []

while True:
    params = {
        "$where": f"crash_date between '{start_date}' and '{end_date}'",
        "$limit": limit,
        "$offset": offset
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    batch = response.json()
    if not batch:
        break

    all_data.extend(batch)
    offset += limit

with open("data/crashes_raw.json", "w") as f:
    f.write(json.dumps(all_data, indent=4))

df = pd.DataFrame(all_data)
df.to_csv("data/chicago_crashes.csv", index=False)

with open("data/chicago_crashes.csv", "rb") as f:
    data = f.read()
    sha256hash = hashlib.sha256(data).hexdigest()

with open("data/chicago_crashes.sha", "w") as f:
    f.write(sha256hash)
