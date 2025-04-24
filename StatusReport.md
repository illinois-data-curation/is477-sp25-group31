## Status Update

As we have had a few weeks to work on our project, this status update is designed to provide information on our progress, changes to the project scope, a description of project artifacts, and a revised timeline.

## Revised Project Goal

Our initial project goal was to assess the impact that weather conditions had on traffic accidents in Chicago from 2020-2025. We have revised the scope of our analysis to only focus on 2025 as we ran into issues obtaining such a substantial amount of data. We will discuss this in more detail later. 

However, our analysis will now focus solely on traffic accidents that have taken place from January 1, 2025, until April 20, 2025. We will address the same questions as we had initially attempted to answer, which are as follows:

1. How do weather conditions impact traffic accident rates in Chicago?
2. Are certain weather types (rain, snow, fog, visibility, etc) associated with higher accident frequency in Chicago?
3. How do accident rates compare between different weather conditions such as clear, rainy, snowy, and foggy days?

Essentially, our analysis will still have the same anticipated outcome just for a smaller period.

## Project Progress

So far, we have completed the data cleaning, merging, and visualization portions of our analysis, which is exactly where we expected to be in terms of progress. We will also provide an updated timeline to ensure that we complete our project by the new deadline, May 8th.

## Obtaining the Data

For our analysis, we are working with two datasets. One is a dataset containing weather records for Chicago, which is from NOAA. This data was publicly available - we simply filtered the data for the dates we were focusing on and imported that into VSCode within the data folder. This will not be visible in the commit history since we are not committing our datasets. 

Our second data set is from the Chicago Data Portal and contains information about traffic accident records in Chicago. We utilized an API key to access the records within this dataset. However, this is where we ran into some issues prompting us to revise our scope. When looking at the data, there were over 500,000 records that related to the 2020-2025 timeframe we were originally looking to evaluate, However, there was a restriction on the number of records we could request utilizing a basic API key. The original limit was 1,000 records, which would simply not be enough for our analysis. After some research, we discovered that we could modify this limit to 50,000 records. This was enough to provide us with all of the traffic accident records in 2025, which is why we chose to revisit our scope. While we did research methods in which we could work around this restriction, we were not able to find a solution to successfully retrieve all 500,000+ records. Therefore, we revised the scope of our analysis to focus only on traffic accidents that have happened from the beginning of 2025 to April 20, 2025, as that consists of approximately 20,000 records. As a result, we were able to avoid any issues with API data record request limitations.

After completing these two sets, we had two raw data files: one for the Chicago weather records and one for the Chicago traffic records. These files are labeled weather_conditions.csv and chicago_crashes.csv within our analysis. We are now ready to move on to data cleaning. 

## Data Cleaning

After obtaining the datasets, the next step in our project was to clean the two datasets. As our research questions were only focused on exploring the correlation between weather and traffic accidents, there were a lot of variables that were unnecessary for our analysis. This included columns such as speed limit, whether drivers ran stop signs/traffic signals, what street the crash occurred on, etc. Therefore, for the Chicago traffic accident data, we decided to drop these columns as they were not relevant to the questions we were looking to answer. However, it is important to realize that the variables that we are dropping could have significantly contributed to the traffic accident. For example, it may be a sunny day, but a driver may have been excessively speeding, leading to an accident. Likely, the accident occurred because of excessive speed in this case. However, we are focused on exploring correlation, not causation through our analysis, so we do not foresee this being a major issue. 

Similarly, for the Chicago weather data, there are many different weather stations that report data for Chicago. Therefore, we decided to group these records and aggregate these statistics so that we could capture average temperatures, winds, precipitation, etc. Furthermore, we had to rename columns so that they would be more descriptive and representative of the data that would be collected for that variable. This included snowfall, average wind speed, haze or fog, etc.

These files are labeled as chicago_weather_cleaned.csv and chicago_crashes_cleaned.csv. After we completed cleaning the data, the next step was to merge the data.

## Data Merging

After we cleaned the two datasets, our focus was to merge these two datasets. We chose to utilize Python instead of SQL to accomplish this step as we had completed cleaning the data in Python as well. Also, since we were working with CSV, JSON, and data frame structures, we chose to utilize Python. After we completed merging the data, we were ready to begin making visualizations.

## Data Visualizations

For our visualization, we wanted to create a geographic heatmap that would take the latitude and longitude of traffic accidents. After conducting some research, we discovered that we could write our visualization into an HTML file, which is what we chose to do. Our visualization displays where in Chicago accidents happen most frequently, ignoring weather conditions. These visualizations are present in the “heatmap.html” and “heatmap.png” files.

## Team Responsibilities

We have split responsibilities fairly evenly throughout the project. While we have worked on it together, the heavier coding and analysis have been done by Ananya using her computer. Therefore, more commits will likely be done by her. Snehal has focused more on the documentation aspect ensuring that we will complete the project on time, including writing the status update. We plan to continue working on the project together in this aspect and use Ananya’s computer to avoid repeating the same data cleaning and merging steps on Snehal’s computer.

## Updated Timeline

We have done a good job of following our original timeline. Our initial goal was to be complete with data cleaning, merging, and visualizations, which we have done thus far. Our next step is to begin automating our workflow and cleaning up documentation. 

Over the next week, we will look to automate our workflow using Snakemake. We anticipate this being completed by April 28th. From there, we will focus on cleaning up our documentation and completing any other aspects of data curation by May 8th, the project deadline. Our documentation will include adding any necessary citations as well as combining steps that we took throughout the data cleaning and merging process. From a workflow automation perspective, we will create a reproducible package, create metadata to describe our package, ensure that our commit history is organized, automate the data acquisition process, and archive our project in a repository to obtain a persistent identifier (directly copied from the project plan). This will likely take us to the end of our project. 

We have achieved significant progress so far on our analysis, and we look to follow the timeline that we have crafted above to ensure that we remain on track while doing a thorough analysis and a proper job of data curation and management. 
