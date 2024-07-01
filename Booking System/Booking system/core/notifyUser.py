import winsound
from core.smsRequest import sendSms

def notify(config):
	out1_ = 'SMS service not enabled'
	out2_ = 'Sound service not enabled'
	if config['notificationDetails']['sms'] ==1:
		out1_ = sendSms(config)
	if config['notificationDetails']['sound'] ==1:
		out2_ = playmusic(config)

	return [out1_,out2_]


def playmusic(config):
	winsound.Beep(config['soundDetails']['frequency'], config['soundDetails']['duration'])
	#fname = "jazz.wav"
	#winsound.PlaySound(fname, winsound.SND_FILENAME)
	return 'sound played'