# Python-Numbeo-webscrap

Designed and implemented a __Numbeo__ (https://www.numbeo.com/cost-of-living/) webscrapper in order to extract information about a specific city and prices for a number of services and goods related to restaurants, markets, transportation, utilities etc.

__Functionality__ :
Given a list of cities the crawler will retrieve information related to the abovementioned. It will then convert the values and concatenate the retrieved information into a single dataframe. Each row represents information about a different city allocated in 55 different features. If the crawler is unable to mine any piece of requested information about a particullar city, it will omit it from the dataframe.
Cities where the cost of living index is not available, it has been registered as 0, they can be used as test set for predictive modelling.

__Aim__
The purpose of this project is to acquire data from various cities and predict the price for services, goods and cost index for cities that there is no related given information. In addition, meaningful information can be extracted through analysis. 

__Storage__
The data is being stored in a MongoDB repository for future usage.
