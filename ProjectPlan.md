# Project Plan

## Overview
The goal of this project is to explore the relationship between weather conditions and traffic accident rates in Chicago from 2020 to 2025 (present day). By integrating weather data and traffic accident records, the project aims to determine whether certain weather conditions (such as rain, snow, visibility, etc) are correlated with increased accident frequencies within Chicago. The insights from this project can help city planners develop safer infrastructure, improve road safety measures, and help traffic management authorities develop better response systems during adverse weather conditions to reduce the number of traffic accidents that may occur as a result.

## Research Questions
1. How do weather conditions impact traffic accident rates in Chicago?
2. Are certain weather types (rain, snow, fog, visibility, etc) associated with higher accident frequency in Chicago?
3. How do accident rates compare between different weather conditions such as clear, rainy, snowy, and foggy days?

## Team Members
- Ananya Vijaykumar
- Snehal Rairikar

## Team Roles and Responsibilities
To begin this project, we created a shared GitHub repository on which we would be able to collaborate. We then concentrated on identifying datasets that we could use to complete our analysis as well as create a list of responsibilities we would have for this project. We will detail this further later in our project plan by describing the datasets we will use as well as outlining a timeline for us to complete the project. The following represents tasks that we have identified and deemed necessary for us to successfully answer our research questions:

### Data Acquisition and Integration
- Identifying credible datasets for traffic and weather data
- Collecting traffic accident data from the City of Chicago Portal
- Retrieving historical weather data using the NOAA API
- Merging datasets using Python to ensure consistency

### Data Profiling and Cleaning
- Performing initial check for data completeness
- Identifying missing values, duplicates, and inconsistencies across both datasets
- Standardizing weather condition fields
- Addressing outliers and other extreme values to improve data quality

### Data Analysis and Visualization
- Analyzing trends and patterns between weather events and accident rates
- Exploring correlations between frequency of accidents and certain weather conditions such as snow and rain
- Creating visualizations such as heatmaps and bar charts to communicate findings

### Documentation
- Maintaining a well-structured markdown documentation for all stages of the project
- Drafting and updating all final deliverables, including the Project Plan (ProjectPlan.md), Status Report (StatusReport.md), and Final Project Report (README.md), following the guidelines of the course
- Documenting all steps to acquire data, decisions made during data cleaning and integration, and overall challenges faced while doing so
- Documenting all steps used to analyze or visualize data
- Ensuring accurate citations of all data and software used in the project
- Create and maintain metadata describing the dataset and software package

### GitHub and Workflow Automation
- Maintaining the project’s GitHub repository
- Ensuring that the commits are well-organized, descriptive, and version-controlled
- Automate data acquisition, integration, and analysis processes using Python
- Archive the final project on Zenodo, generating a persistent identifier for reproducibility

The tasks outlined above will be completed through collaboration between both team members. Ananya will take the lead on Data Acquisition and Integration as well as Data Profiling and Cleaning. Snehal will take the lead on Data Analysis and Visualization and Documentation. The responsibilities related to GitHub and Workflow Automation will be purely collaborative, requiring both Ananya and Snehal to actively contribute throughout the execution of the project.

## Identifying and Describing Datasets:
We have identified 2 datasets that will assist us in answering our research questions. 
The first dataset is an API from NOAA. This dataset is titled “Daily Summaries Location: Chicago, IL, US, City:17006.”  The dataset contains weather records for Chicago dating from 1870 and includes information about air temperature, precipitation, cloud coverage, and weather type in addition to many other variables; however, these are the ones we see being most relevant to our analysis. Our project will focus on the time period ranging from 2020-2025, which means that we will have to filter or adjust our data accordingly when conducting our analysis. 
Link to Dataset: https://www.ncdc.noaa.gov/cdo-web/datasets/GHCND/locations/CITY:US170006/detail 

The second dataset is from the Chicago Data Portal titled “Traffic Crashes”. This dataset contains all Chicago traffic accident records, including information on date, weather, lighting, road conditions, latitude, longitude, and more variables; however, these are the variables we see being most relevant to our analysis. Additionally, the records from this dataset date back to 2013. Since our analysis is only focusing on 2020 to 2025, we will have to adjust and filter the data accordingly prior to performing any data integration. 
Link to Dataset: https://data.cityofchicago.org/Transportation/Traffic-Crashes-Crashes/85ca-t3if/about_data 

Taking a closer look at both datasets, there are a few interesting points for discussion. First, there is already a weather column present in the Chicago Traffic Accident data. When integrating the two datasets, we would merge them based on date. This would result in a one-to-many relationship from an entity-relationship perspective as there is one weather record for each day, and there are multiple traffic accidents taking place each day. 
Both datasets are available for public use, placing no restrictions on usage, as the NOAA API and Chicago Data Portal are in the public domain. The licenses do not differ for these datasets.

## Timeline:
We have outlined our roles and responsibilities above. Additionally, we have confirmed that we have created our shared Github project repository along with selecting our datasets and identifying our research questions in the first 3 weeks. Below, we will outline the remaining tasks that we need to complete for our project. This will be detailed as a timeline to ensure that we complete all aspects of the project prior to the deadline.

We will spend the week of April 7th (Week 4) integrating, profiling, and cleaning our datasets. This will include merging the two datasets based on date as well as addressing any issues with “dirty data”. We anticipate there being weather and traffic accident records that are incomplete or inaccurate, so we will take a thorough look at all records when completing this step. 

In the following week (Week 5 - Week of April 14th), we will focus on implementing our data analysis and visualizations. This will include our initial insights on what weather conditions are most prone to traffic accidents. Additionally, we will construct our heatmap to detail where accidents took place and how that is correlated to weather conditions. 

Starting the week of April 21st (Week 6), we will focus on cleaning up our documentation and automating our workflow. We anticipate this step taking us to the end of our project and to our project deadline of May 1st. Our documentation will consist of tracking all steps taken during data integrating, profiling, and cleaning steps, as well as adding necessary citations. From a workflow automation perspective, we will create a reproducible package, create metadata to describe our package, ensure that our commit history is organized, automate the data acquisition process, and archive our project in a repository to obtain a persistent identifier. This will ensure that our end-to-end workflow execution is automated.

By following the timeline above, we believe we can complete a comprehensive analysis and answer the research question we are looking to answer.     
