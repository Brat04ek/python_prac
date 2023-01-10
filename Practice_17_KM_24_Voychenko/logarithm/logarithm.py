from math import log as logorithm, e as math_e

def log(a, b):
	try:
		a, b = float(a), float(b)
		if a>0 and a!=1 and b>0:
			return logorithm(b, a)
		else: raise ValueError()
	except:
		return 'Error'

		
def ln(b):
	try:
		b = float(b)
		if b>0:
			return logorithm(b, math_e)
		else: raise ValueError()
	except:
		return 'Error'

def lg(b):
	try:
		b = float(b)
		if b>0: 			
			return logorithm(b, 10)
		else: raise ValueError()
	except:
		return 'Error'