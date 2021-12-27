import requests
import pymongo
import logging
import pandas as pd
from bs4 import BeautifulSoup


class NumbeoScraper:
    
	def __init__(self):
		logging.basicConfig(filename='example.log', level=logging.DEBUG)
		logging.debug('Scrapper initialised')
		self.client = pymongo.MongoClient("mongodb+srv://Giorgos:Uplifting7@cluster0.1gk0o.mongodb.net", 
		                 tls=True,
		                 tlsAllowInvalidCertificates=True)
		self.db = self.client["scrape_db"]
		self.collection = self.db["cities"]

	def get_costs(self,city,currency):
		try:
			self.city = city
			page = requests.get("https://www.numbeo.com/cost-of-living/in/" + self.city)
			soup = BeautifulSoup(page.content)
			data = soup.find_all("table",{"class":"data_wide_table new_bar_table"})
			html_parsed = [item.text.split(currency) for item in data]
			flat_list = [item for sublist in html_parsed for item in sublist]
			clean = [item for item in str(flat_list).split('\\n\\') if len(item)>35]
			processed = [item.replace('\\xa0₴', '').replace("\\xa0', '","").replace('Edit \\', '').replace('n\\n', '').replace('n1 ', '').replace('1 ', '') for item in clean]
			self.final = [item.strip("n") for item in processed]
			logging.info('%s %s', 'Fetched info for', self.city)
		except Exception as e:
			logging.info(str(e))

	def create_df(self):
		try:
			self.df = pd.DataFrame(self.final,columns=['total'])
			self.df[['Service', 'Cost']] = self.df['total'].str.split('  ', 1, expand=True)
			self.df.drop(['total'],axis=1,inplace=True)
			self.df['city'] = self.city
			logging.info('Dataframe created')
			return self.df
		except Exception as e:
			logging.info(str(e))

	def insert_mongo(self):
		try:
			self.db.self.collection.insert_many(self.df.to_dict('records'))
			logging.info('Data inserted in db')
		except Exception as e:
			logging.info(str(e))

	def select_item(self,field,value):
		try:
			resp = self.db.self.collection.find_one({field:value})
			return print(resp)
		except Exception as e:
			logging.info(str(e))