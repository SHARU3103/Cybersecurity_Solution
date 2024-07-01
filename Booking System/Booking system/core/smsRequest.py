import requests

def sendSms(config):
	url = config['fast2smsDetails']['metaData']['url']
	querystring = {
		"authorization":config['fast2smsDetails']['metaData']['authorization'],
		"sender_id":config['fast2smsDetails']['metaData']['sender_id'],
		"message":config['fast2smsDetails']['data']['message'],
		"language":config['fast2smsDetails']['metaData']['language'],
		"route":config['fast2smsDetails']['metaData']['route'],
		"numbers":config['fast2smsDetails']['data']['numbers']
	}
	headers = {
    	'cache-control': "no-cache"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)

	return response.text

"""
Doc: https://docs.fast2sms.com/?python#overview
Response Code	Status Code	      Message
    400            401	       Sender ID Missing
    400            402	       Message Text Missing
    400            403	       Route Missing
    400            404	       Language Missing
    400            405	       Numbers Missing
    400            406	       Invalid Sender ID
    400            407	       Invalid words used in message
    400            408	       Invalid Route
    400            409	       Invalid Route Authentication
    400            410	       Invalid Language
    400            411	       Invalid Numbers
    401            412	       Invalid Authentication, Check Authorization Key
    401            413	       Invalid Authentication, Authorization Key Disabled
    400            414	       IP is blacklisted from Dev API section
    400            415	       Account Disabled
    400            416	       You don't have sufficient wallet balance
    400            417	       Use english letters or change language to unicode
    400            418	       Invalid Quick Transactional Template ID.
    400            419	       Quick Transactional Template Variables Missing
    400            420	       Invalid Quick Transactional Variables
    400            421	       Quick Transactional Template Variable Values Missing
    400            422	       Invalid Variable Values or Some Values Missing
    400            423	       Transactional Route is active, Use Bulk SMS API.
"""	