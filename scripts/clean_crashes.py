import pandas as pd
import hashlib

#cleaning crash data
df_crash = pd.read_csv("data/chicago_crashes.csv")

columns_to_drop = [
    "crash_date_est_i", "posted_speed_limit", "traffic_control_device", "device_condition",
    "first_crash_type", "trafficway_type", "lane_cnt", "alignment", "road_defect",
    "report_type", "crash_type", "intersection_related_i", "not_right_of_way_i",
    "hit_and_run_i", "damage", "date_police_notified", "prim_contributory_cause",
    "sec_contributory_cause", "street_no", "street_direction", "street_name",
    "beat_of_occurrence", "photos_taken_i", "statements_taken_i", "dooring_i",
    "work_zone_i", "work_zone_type", "workers_present_i", "num_units",
    "most_severe_injury", "injuries_fatal", "injuries_incapacitating",
    "injuries_non_incapacitating", "injuries_reported_not_evident",
    "injuries_no_indication", "injuries_unknown", "crash_hour",
    "crash_day_of_week", "crash_month", "private_property_i"
]
df_crash = df_crash.drop(columns=columns_to_drop, errors="ignore")
df_crash.to_csv("data/chicago_crashes_cleaned.csv", index=False)
df_crash["crash_date"] = pd.to_datetime(df_crash["crash_date"]).dt.date
