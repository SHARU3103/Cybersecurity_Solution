from bs4 import BeautifulSoup as bs 
import requests
from tqdm import tqdm
import time



def is_link_available(soup):
    
	k = soup.find('div',{"class":"right-content"})
	#print(k.find('div',{'class':"action-book"}))
	
	check = False
	try:
		if k.find('div',{"class":"more-showtimes"}):
			check = True
	except:
		pass
	return check

def checkAvailability(config):
	i = 0
	while True:
		source = requests.get(config['showDetails']['data']['movieLink'])
		time.sleep(1)
		soup = bs(source.content,"html.parser")
		if is_link_available(soup):
			print('Link Found')
			return True
		else:
			if i%30==0:
				print('Time Passed Approx(in Minutes): ',(i*20)//60)
			i+=1
			time.sleep(config['showDetails']['metaData']['sleepTime'])
