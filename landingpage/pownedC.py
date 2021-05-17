import hashlib 
import requests
import argparse

class Powned():

	def __init__(self , pwdString):
		self.pwdString = pwdString
		self.FOUND_STRING = '''your password was found: \n - Hash {password_hash} \n -Occurences : {occurrences}'''

		self.NOT_FOUND_STRING = "your password wasn't found"
		
	def hashIt(self):
		sha1 = hashlib.sha1()
		sha1.update(self.pwdString.encode('utf-8'))
		hash_pass = sha1.hexdigest().upper()
		return hash_pass
	
	def checkPownedAPI(self):
		url = "https://api.pwnedpasswords.com/range/{}".format(self.hashIt()[:5])
		list_of_hashes = requests.get(url=url).text.split("\r\n")

		found_password = False

		# Check all hashes in the array, until a matching one is found or none are left, print the result
		for foundHash in list_of_hashes:
			split = foundHash.split(":")
			if self.hashIt()[5:] == split[0]:
				occurrences = "1 occurrence" if split[1] == "1" else "{:,d} occurrences".format(int(split[1]))
				found_password = True
				return self.FOUND_STRING.format(password_hash=self.hashIt(), occurrences=occurrences)
				break
		if not found_password:
			return False
