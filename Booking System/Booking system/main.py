from helper._helperFunc import readConfig
from core.bookMyShowRequest import checkAvailability
from core.notifyUser import notify

def printDetails(config):
	print('\n\nMovie Link :',config['showDetails']['data']['movieLink'])
	print('Sleep time after every failed request(in Second) : ',config['showDetails']['metaData']['sleepTime'])
	print('Message on Success :',config['fast2smsDetails']['data']['message'])
	if config['notificationDetails']['sms'] ==1:
		print('Subscribed to SMS\nMobile Numbers :',config['fast2smsDetails']['data']['numbers'])
	else:
		print('Not subscribed to SMS service')
	if config['notificationDetails']['sound'] ==1:
		print('Subscribed to Sound service\n\n')
	else:
		print('Not subscribed to sound service\n\n')


def main():
	config = readConfig()
	printDetails(config)
	out_ = checkAvailability(config)

	if out_:
		temp_=notify(config)
		print(temp_[0])

main()
