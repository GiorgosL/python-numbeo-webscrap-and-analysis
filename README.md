# Python-Numbeo-webscrap

Designed and implemented a __Numbeo__ (https://www.numbeo.com/cost-of-living/) webscrapper in order to extract information about a specific city and prices for a number of services and goods related to restaurants, markets, transportation, utilities etc, as well as its index cost.

__Functionality__ :
Given a list of cities the crawler will retrieve information related to the abovementioned. It will then convert the values and concatenate the retrieved information into a single dataframe. Each row represents information about a different city allocated in 55 different features. If the crawler is unable to mine any piece of requested information about a particullar city, it will omit it from the dataframe.
Cities where the cost of living index is not available, it has been registered as 0, they can be used as test set for predictive modelling.

__Aim__
The purpose of this project is to acquire data from various cities and predict the price for services, goods and cost index for cities that there is no related given information. In addition, meaningful information can be extracted through analysis. 






consumer_key="z6NNNbcgLTR6cKTU87yq75qC9"
consumer_secret="eXPAthJgm6s089idPp02444munJf0jFgTcIf1ipVyp714m70y2"
access_token="1044683220472811522-96CTfG9s3Ik88LVzKmgYx6zq1rBsSr"
access_token_secret="H4u7pX3LfendkD4QY2eAeFK2xfBnRuqRmQuUaXe5WCWsz"
