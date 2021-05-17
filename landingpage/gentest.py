import string 
from random import choice

def passgen():
	symb = """!#$%&'()*+,-./:";<=>?@[\]^_`{|}~"""
	chars = string.letters + string.digits + synmb 
	passchar = ''.join(choice(chars) for _ in xrange(15))
	return passchar 
