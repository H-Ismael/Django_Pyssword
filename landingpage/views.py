from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from django.contrib import messages
from . import pyssword , pownedC , gen

def plvl(respstr):

	p1 = pyssword.Cpwd(respstr)
	pscore = p1.scoreEq()

	if pscore == 0 :
		return 'Your password should not have space or be less than 7 charachters'
	elif 0 < pscore  <= 0.5:
		return 'Your password is weak'
	elif 0.5 < pscore  <= 0.75 :
		return 'You password stenght intermediate'
	elif 0.75 < pscore  <= 1 :
		return 'You password is strong'
	else :
		return 'Yomething went wrong during the checking process'

def captcha(respcap):

	if respcap.method == 'POST':
		cap_token = respcap.POST.get("g-recaptcha-response")
		cap_url = "https://www.google.com/recaptcha/api/siteverify"
		cap_key = "6LeH2qEaAAAAACindTMoKEsMTGZIoibRYT8hiT7S"
		cap_data = {"secret": cap_key , "response": cap_token}
		cap_server_resp = requests.post(url=cap_url ,data = cap_data)
		cap_json = json.loads(cap_server_resp.text)
		#capj = cap_json['success']

		return cap_json['success']

def isponed(pstr):
	
	pownedclss = pownedC.Powned(pstr)
	pwndStr = pownedclss.checkPownedAPI()
	
	if pwndStr == False :
		return ' \n Password occurences : None'
	else : 
		return pwndStr

def index(response):
	passlvl = ""
	powned = ""
	passgen = ""
	if response.method == "POST" and "form1" in response.POST:

		if captcha(response) == True: 

			pwdStr = response.POST['pass1']
			passlvl = plvl(pwdStr)
			powned = isponed(pwdStr)
			#newreponse = '\n' + passlvl + '\n' + powned

		else:
			messages.error(response , "Captcha was not validated")

	if response.method == "POST" and "form2" in response.POST:

		if captcha(response) == True: 

			passgen = gen.passgen()

		else:
			messages.error(response , "Captcha was not validated")

		

	return render(response,'index.html',{"passlvl": passlvl , "powned": powned , "genp": passgen})