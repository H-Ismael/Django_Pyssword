import string 
from random import choice

def passgen():
	symb = """!#$%&'()*+,-./:";<=>?@[\]^_`{|}~"""
	chars = string.ascii_letters + string.digits + symb 
	passchar = ''.join(choice(chars) for _ in range(15))
	return passchar
