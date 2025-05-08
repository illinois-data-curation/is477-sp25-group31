# **Weather and Traffic Accidents in Chicago (2025)**

## **Link to Archival Record**

* \[Zenodo DOI Placeholder – Replace with actual link once uploaded\]

## **Contributors**

* Ananya Vijaykumar  
* Snehal Rairikar

## **Summary**

The goal of this project is to explore the relationship between weather conditions and traffic accident rates in Chicago from January 1, 2025, to April 20, 2025\. By integrating weather data and traffic accident records, the project aims to determine whether certain weather conditions (such as rain, snow, visibility, etc) are correlated with increased accident frequencies within Chicago. The insights from this project can help city planners develop safer infrastructure, improve road safety measures, and help traffic management authorities develop better response systems during adverse weather conditions to reduce the number of traffic accidents that may occur as a result.

Initially, our project intended to cover a five-year period spanning 2020 to 2025\. However, after encountering some technical issues, primarily related to limits on API requests, we adjusted the scope of our analysis to focus only on the year 2025\. This was a good decision because it allowed us to work with a more manageable amount of data. In saying that, the data was still substantial, which helped us ensure the integrity and reproducibility of our workflow. Within this new scope, we obtained and analyzed over 20,000 traffic crash records. Despite narrowing the time frame, this dataset provided enough variability in both weather and accident types to create meaningful insights.

To address our research questions, we collected data from two key sources. One is a dataset containing weather records for Chicago, which is from the NOAA weather API. This data was publicly available \- we simply filtered the data for the dates we were focusing on and imported that into VSCode. Our second data set is from the Chicago Data Portal and contains information about traffic accident records in Chicago. We utilized an API key to access the records within this dataset. As mentioned earlier, we ran into some API limit restrictions, which led to us changing our scope. 

This gave us two raw datasets, which we then applied data cleaning procedures to. For the crash data, we dropped columns that were not relevant to the questions we were looking to answer. However, it is important to realize that the variables that we are dropping could have significantly contributed to the traffic accident. For the weather data, there are many different weather stations that report data for Chicago. Therefore, we decided to group these records and aggregate these statistics so that we could capture average temperatures, winds, precipitation, etc. Furthermore, we had to rename columns so that they would be more descriptive and representative of the data that would be collected for that variable. After cleaning, we merged the two datasets using Python.

After doing so, we used tools like pandas, seaborn, and matplotlib for data processing and visualization. We also implemented an automated workflow using Snakemake to ensure that the entire process, from data acquisition and merging to analysis and visualization, could be reproduced in a structured and reliable manner. 

Our results showed that clear weather days had the highest total number of crashes, likely because more people drive in good conditions. However, when looking at crashes per day, bad weather like rain or snow was clearly linked to more frequent accidents. These insights could help the city of Chicago improve traffic safety by adjusting signals or issuing public warnings when bad weather is expected.

Our full project, including scripts, metadata, visualizations, and workflow automation, has been archived on Zenodo and is accessible for public reuse.

## **Data Profile**

We used two distinct datasets in our project to answer the research questions.

1. **NOAA Weather Data (Daily Summaries \- Chicago, IL)**  
   * **Source**: NOAA’s National Centers for Environmental Information (NCEI)  
   * **URL**: [https://www.ncdc.noaa.gov/cdo-web/datasets/GHCND/locations/CITY:US170006/detail](https://www.ncdc.noaa.gov/cdo-web/datasets/GHCND/locations/CITY:US170006/detail)   
   * **License**: Public domain. No restrictions on use. This means the data source explicitly allows the public to use, share, modify, and distribute the data freely and without needing permission.  
   * **Description**: This dataset, titled “Daily Summaries Location: Chicago, IL, US, City:17006,” provides historical weather measurements from multiple NOAA-operated weather stations throughout the Chicago area. The records date back to 1870 and include variables such as air temperature (in tenths of degrees Celsius), daily precipitation (mm), snowfall (mm), average wind speed (m/s), and boolean indicators for weather such as fog, haze, ice pellets, glaze, and high/damaging winds. For this project, we filtered the dataset to include only the dates between January 1, 2025, and April 20, 2025\. Since there are multiple weather stations per day, we chose the weather station that was most relevant to our research. Before using this data, we needed to choose the most appropriate columns to work with. For most weather conditions, we decided to use the numerical columns. Within the numeric columns, we used the average values to ensure the accuracy of our research. All these steps allowed us to build a clean dataset to match crash records for the same time period.  
2. **Traffic Crash Data (City of Chicago Data Portal)**  
   * **Source**: City of Chicago Open Data Portal  
   * **URL**: [https://data.cityofchicago.org/Transportation/Traffic-Crashes-Crashes/85ca-t3if/about\_data](https://data.cityofchicago.org/Transportation/Traffic-Crashes-Crashes/85ca-t3if/about_data)   
   * **License**: Public domain. No restrictions on use. This means the data source explicitly allows the public to use, share, modify, and distribute the data freely and without needing permission.  
   * **Description**: The second dataset is titled “Traffic Crashes.” It contains detailed crash records from across the City of Chicago, including over 1 million entries dating back to 2013\. Each record has attributes such as the crash timestamp, weather conditions at the time, lighting conditions, road surface type, number of injuries, and geographic coordinates (latitude/longitude). For our project, we accessed this data using the Socrata Open Data API and filtered it programmatically to retrieve only the 2025 records (January 1 – April 20), resulting in a dataset of \~20,000 crashes. We retained only variables directly related to our research questions (e.g., weather, lighting, surface, injuries), and removed those unrelated (e.g., street names, posted speed limits). The cleaned dataset gave us a focused view of crash patterns, which we then linked to daily weather summaries for correlation analysis.

These datasets were programmatically filtered and then merged by date, creating a one-to-many relationship where each weather record was joined to all crash records on the same date. This integration allowed us to perform a detailed analysis that directly connects weather conditions to traffic crashes in Chicago. By focusing on just the first few months of 2025, we were able to produce a clean and manageable dataset that still provided diverse enough data to reveal meaningful trends. This new timeline is especially useful because it reflects the most recent traffic patterns, making our findings more relevant and applicable to current safety planning.

## **Findings**

We centered our findings around finding patterns and trends between traffic accidents and weather. By analyzing these factors, we will be able to gather insights on how weather contributes to, or lacks, contributing to traffic safety. Furthermore, we can deeply analyze what factors may contribute to traffic accidents, and what can be done to reduce this number in the future. City officials can use these findings to improve public safety procedures, roadway hazards, and traffic rules to ensure that the greatest number of people are safe. Here are the key findings that our analysis produced:

* **Crash frequency is highest during clear weather**, which initially seems counterintuitive. However, this can be explained by higher traffic volume on clear days, leading to a higher baseline number of accidents. This likely suggests that there may be other factors that contribute to these accidents, such as speeding, reckless driving, running a stop sign, etc. Our analysis demonstrates correlation and not causation that more accidents are correlated with clear weather..  
* **Weather types like rain and snow are associated with higher per-day crash rates**. Days with measurable precipitation, snowfall, or fog saw significantly more accidents compared to days without such conditions. While these weather conditions occurred less frequently, they contributed to more accidents per day, likely due to hazardous conditions. While again this merely demonstrates correlation, there were more accidents occurring per day because of this, likely due to reduced visibility, increased braking distances, less traction control, etc. Freezing rain specifically had the highest crash per day rates suggesting that this weather may have posed adverse weather conditions.   
* **Rainy conditions consistently led to increased crash occurrences**, especially freezing rain contributed to a higher number of accidents. Both freezing rain and rain contributed to a significant number of traffic accidents, ranking first and fourth, respectively, in the highest crash per day rates. These weather conditions likely resulted in reduced visibility and increased road slickness during those times. While the weather conditions may not have been the sole cause of these accidents, they certainly may have been a contributing factor, as there is a clear trend present.   
* **Injuries were slightly more common in crashes that occurred during adverse weather**, although this relationship is weaker and may require further investigation. There are typically a higher number of accidents per day correlated with adverse weather conditions, which would suggest a higher number of injuries. However, there can also be occurrences where one accident contributes to several injuries, which is not exactly depicted through our analysis \- something we can explore in the future.   
* **Unknown/Other, which includes weather conditions that are mixed or unclear, also contributes to a significant amount of traffic accidents:** Unknown and other weather conditions rank fifth and seventh, respectively, in traffic accidents per day. While the weather is not likely to be unknown, this could include data that was not reported or accidents that were present in a combination of weather conditions. Whatever the case may be, these conditions contributed to a significant number of traffic accidents as well as material that can be reviewed by city officials to improve traffic safety.

These findings suggest that while overall crash numbers are higher during good weather due to increased driving activity, poor weather introduces additional risk factors that significantly elevate accident rates on a per-day basis.

## **Future Work**

**Lessons Learned:**  
Through this project, we learned a few key lessons that will help us in our future data science projects.

* Adjusting our scope to our needs: We learned the importance of being flexible with our project scope. During our project, we ran into an unexpected hurdle. We were not previously aware that obtaining data through an API key would have data limitations. Originally, we wanted to use crash data from 2020 to 2025; however, due to API restrictions and data size constraints, we had to quickly adapt. Instead of getting stuck, we shifted our focus to just the first few months of 2025\. This also taught us the importance of adapting our project goals when faced with unforeseen circumstances. This shift allowed us to continue working on our analysis without getting overwhelmed. It also gave us a more manageable workload so that we could produce more meaningful results.  
* Limitations of working with large-scale open data: We also learned important lessons around the practical limitations of working with large-scale open data, including API key limitations, untidy data and data cleaning, and joining mismatched formats. It is difficult to access a large number of data records via an API key; therefore, having a narrow project scope is essential to conducting a useful data analysis. We also learned that data cleaning is a major component of an analysis project, as we need to have tidy data to conduct a proper and useful analysis. Through this, we were able to improve our technical skills and derive stronger insights.   
* Designing visualizations to match our project goals: Another lesson we learned was how to make relevant visualizations that support our analysis more clearly. Initially, we tried to make a lot of different visualizations, but not all of them helped us understand our data better or were relevant to our research questions. At the start of our project, we wanted to learn how to make an interesting heatmap to understand the density of traffic accidents in different regions of Chicago. While creating this visualization taught us something new, we also soon realized that it was not contributing to answering our research question. Eventually, we focused on using a simpler visualization, like a bar chart, that directly addressed our research question. This new visualization made it easier for us, and anyone else, to understand our project more clearly. Finally, it taught us that while it could be interesting to try out different visualizations, we need to ultimately choose the visualization that best suits our project goals.

**Future Work:**

While our project is only limited to a four-month window of data from 2025, it opens the door to conducting additional analysis: . 

* **Longitudinal Analysis**: Due to an API key restriction, we were only able to obtain 50,000 traffic accidents records. However, if there is a different data source containing the same information without these restrictions, we may be able to expand our analysis. By analyzing multiple years’ worth of weather and crash data could confirm and strengthen our findings.  
* **Severity Modeling**: While our analysis focused solely on the correlation between weather and traffic accidents, we could explore answering other topics, such as the correlation between injuries and weather conditions. By adding variables related to injury severity and medical outcomes, we could gain a deeper understanding of the trends of traffic accidents as well as what can be done to reduce the risk of severe accidents.  
* **Predictive Modeling**: We see a correlation between weather conditions and traffic accidents, which is something we want to further explore. Building machine learning models can help to predict crash likelihood based on weather forecasts, which can have real-world applications. If thoroughly developed, these are models that can be used by navigation and other mapping systems to help reduce the total number of traffic accidents. 

**Reproducing**

Follow these steps to reproduce our workflow:

1. **Clone the Repository**:

git clone [https://github.com/illinois-data-curation/is477-sp25-group31](https://github.com/illinois-data-curation/is477-sp25-group31)   
cd is477-sp25-group31

2. **Download the Data**:

Retrieving data: Create a data folder.

1. From the API key  
* **Obtain an API Key**  
  * Visit the City of Chicago Data Portal and generate an App Token.  
  * Save your token in a file named `chicago_api.txt` in your project root. It should contain just one line with the token.  
* **Run the Data Retrieval Script**  
  * Run chicago\_accidents\_retreiving\_data.py  
* **Verify File Integrity**

  * The script also generates a SHA-256 hash file (`chicago_crashes.sha`) for data integrity.  
2. From NOAA  
* Go to [https://www.ncdc.noaa.gov/cdo-web/datasets/GHCND/locations/CITY:US170006/detail](https://www.ncdc.noaa.gov/cdo-web/datasets/GHCND/locations/CITY:US170006/detail)  
* Select “Add to cart.”  
* Under “Select output format,” select “Custom GHCN-Daily CSV.”  
* Select date range as 2025-01-01 to 2025-04-20  
* Click “Continue.”  
* Click all the checkboxes under “Station Detail & Data Flag Options” and “Select data types for custom output.”  
* Review your selected options  
* Enter email address  
* Submit order  
* Drag and drop the downloaded file and place it in the `/data` directory.  
    
3. **Install Dependencies**:

pip install \-r requirements.txt

4. **Run Workflow**:

snakemake \--cores 1 all

5. **View Results**:  
* Visualizations will be stored in the `/results` directory, saved under the name `normalized_weather_crashes.png`  
* OPTIONAL: Visit our Box folder [https://uofi.box.com/s/jjj1lf6xf4394jwqykxudsfzo2034c4p](https://uofi.box.com/s/jjj1lf6xf4394jwqykxudsfzo2034c4p)  to download and view our output.

## **References**

* NOAA National Centers for Environmental Information. Daily Summaries Dataset: [https://www.ncdc.noaa.gov/cdo-web/datasets/GHCND/locations/CITY:US170006/detail](https://www.ncdc.noaa.gov/cdo-web/datasets/GHCND/locations/CITY:US170006/detail)  
* City of Chicago Open Data Portal. Traffic Crashes: [https://data.cityofchicago.org/Transportation/Traffic-Crashes-Crashes/85ca-t3if/about\_data](https://data.cityofchicago.org/Transportation/Traffic-Crashes-Crashes/85ca-t3if/about_data) 

