import sys

class Cpwd:

	gScore = 0 
	
	
	def __init__(self , pwdString):
		self.pwdString = pwdString 
		self.symbolstring = """!#$%&'()*+,-./:";<=>?@[\]^_`{|}~"""	
		
	def alph(self):
			
		if any(s.isupper() for s in self.pwdString) and any(s.islower() for s in self.pwdString):
			salpha = 2
		elif any(s.isalpha() for s in self.pwdString):
			salpha = 1
		else:
			salpha = 0
		
		return salpha
	
	def num(self):
		if any(s.isdigit() for s in self.pwdString):
			return 1
		else : 
			return 0
	def symb(self):
		if any(s in self.symbolstring for s in self.pwdString):
			return 1
		else : 
			return 0
	
	def scoreEq(self):
		scoreEq = self.cF() * self.cC()
		
		return scoreEq
		
	def pwdLenCheck(self):
		if (not any(l.isspace() for l in self.pwdString)) and (len(self.pwdString) > 7) and (len(self.pwdString) < 25) :
			return 1
		else : 
			return 0 
			
	def cF(self):
		return self.pwdLenCheck()
		
	def cC(self):
		
		return (self.alph() + self.num() + self.symb())/4
		

'''
pc = Cpwd(sys.argv[1])
print(pc.scoreEq())
	'''	
		
