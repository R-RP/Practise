we will be analyzing some 911 call data from [Kaggle](https://www.kaggle.com/mchirico/montcoalert). The data contains the following fields:

* lat : String variable, Latitude
* lng: String variable, Longitude
* desc: String variable, Description of the Emergency Call
* zip: String variable, Zipcode
* title: String variable, Title
* timeStamp: String variable, YYYY-MM-DD HH:MM:SS
* twp: String variable, Township
* addr: String variable, Address
* e: String variable, Dummy variable (always 1)

Problem Statement:

1.What are the top 5 zipcodes for 911 calls?
2.What are the top 5 townships (twp) for 911 calls?
3.how many unique title codes are there?
4.create a new column called "Reason" that contains this string value of "Reasons/Departments" specified before the title code in the "title" column
5. What is the most common Reason for a 911 call based off of this new column?
6.Visualise 911 calls based on reason.
7.Convert "timestamp" column into datetime object and create 3 new columns for 'Hours' ,'Month' & 'Day of the week'.
8.Visualise the 'Reason' distribution for every day of the week and distribution for every month.
9.Visualise line plot for calls per month.
10.Finaly create a heatmap of "day of the week" vs "hour of the day" and "day of the week" vs "Months of the year". 