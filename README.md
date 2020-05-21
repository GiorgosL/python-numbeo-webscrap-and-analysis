# Python-Numbeo-webscrap-and-modelling

Designed and implemented a __Numbeo__ (https://www.numbeo.com/cost-of-living/) webscrapper in order to extract information about a specific city, cost of living index and prices for a number of services and goods related to restaurants, markets, transportation, utilities etc.

__Cost of living index__ :
Is measured against New York city, meaning NYC has a cost index of 100 and the remaining cities get their cost of living index with regards to how much more or less expensive are compared to NYC.


__Functionality__ :
Given a list of cities the crawler will retrieve information related to the abovementioned. It will then convert the values and concatenate the retrieved information into a single dataframe. Each row represents information about a different city allocated in 55 different features. If the crawler is unable to mine any piece of requested information about a particullar city, it will omit it from the dataframe.
Cities where the cost of living index is not available, it has been registered as 0, they can be used as test set for predictive modelling.

__Aim__
The purpose of this project is to acquire data from various cities and predict the price for services, goods and cost index for cities that there is no related given information. In addition, meaningful information can be extracted through analysis. However, since the cities spawn across EU and USA a currency convertion has been applied.
