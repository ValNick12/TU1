import math

def pinus(prec):
	sum = 0
	for i in range(prec):
		sum += (-1)**i / (2 * i + 1)
	return sum * 4
	
prec = int(input('Sloji mi qnko:'))

print(pinus(prec))

