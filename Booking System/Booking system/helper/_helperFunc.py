import json


def readConfig():
	with open('./config/data.json') as f:
		d = json.load(f)
	return d