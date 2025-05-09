## Merged data column descriptions

| Column Name                 | Description                                                                 | Data Type   | Example              |
|-----------------------------|-----------------------------------------------------------------------------|-------------|----------------------|
| crash_record_id             | Unique identifier for the crash record                                     | String      | 6720b1c8a78e5c3b55e749ed49827993737900a5fad5ded5335ec7fa1e6ce91ea9926f3a00f52c119b532c84f1f8252fe1722624f9ccf5a23e50cc6c3c689638        |
| crash_date                  | Date and time when the crash occurred                                      | Timestamp   | 2025-04-20 23:59:00  |
| weather_condition           | Description of weather at the time of crash (from crash data)              | String      | RAIN, CLEAR          |
| lighting_condition          | Lighting conditions at the crash site                                      | String      | DARKNESS, DAYLIGHT   |
| roadway_surface_cond        | Surface condition of the road at the time of crash                         | String      | WET, DRY             |
| injuries_total              | Total number of injuries reported from the crash                           | Float       | 1.0                  |
| latitude                    | Latitude coordinate of the crash                                           | Float       | 41.6642489615        |
| longitude                   | Longitude coordinate of the crash                                          | Float       | -87.6283560813       |
| location                    | GeoJSON point representation of crash location                             | String      | "{'type': 'Point', ...}" |
| avg_wind_speed_mps          | Average wind speed for the day in meters per second                        | Float       | 0.0                  |
| precipitation_mm            | Total daily precipitation in millimeters                                  | Float       | 0.0                  |
| snowfall_mm                 | Total daily snowfall in millimeters                                       | Float       | 0.0                  |
| fog_or_freezing_fog         | Binary flag indicating presence of fog or freezing fog (1=yes, 0=no)       | Float       | 0.0                  |
| heavy_fog_or_mist           | Binary flag indicating presence of heavy fog or mist                       | Float       | 0.0                  |
| thunderstorms               | Binary flag indicating thunderstorms                                       | Float       | 0.0                  |
| ice_pellets_or_small_hail   | Binary flag for presence of ice pellets or small hail                      | Float       | 0.0                  |
| hail_large                  | Binary flag indicating large hail presence                                | Float       | 0.0                  |
| glaze_or_rime               | Binary flag for presence of glaze or rime ice                              | Float       | 0.0                  |
| smoke_or_haze               | Binary flag indicating presence of smoke or haze                           | Float       | 0.0                  |
| blowing_or_drifting_snow    | Binary flag for drifting/blowing snow                                      | Float       | 0.0                  |
| high_or_damaging_winds      | Binary flag for high or damaging wind conditions                           | Float       | 0.0                  |
| avg_temp_tenths_C           | Average daily temperature in tenths of a degree Celsius (e.g., 125 = 12.5) | Integer     | 125                  |
