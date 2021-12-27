#!/usr/bin/env python
# coding: utf-8
from scraper import *
from flask import Flask, request, jsonify
import pickle
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/predict',methods=['POST'])
def predict():
	data = request.json
	ns.get_costs(data['city'],data['currency'])
	df = ns.create_df()
	ns.insert_mongo()
	return jsonify(df.to_dict(orient="records"))

@app.route('/query',methods=['POST'])
def retrieve():
	data = request.json
	key, val = next(iter(data.items()))
	ns.select_item(key,val)
	return ''

if __name__ == '__main__':
	ns = NumbeoScraper()
	logging.info('App starting')
	app.run(debug=True)