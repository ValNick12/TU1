from math import pi, sin

EPS = 1 - 6

x = float(input('x[deg]='))
xrad = x/180*pi

an_1 = 0
an = xrad
sinx = 0
counter = 3
sign = -1

while abs(an-an_1)>=EPS:
    sinx += an
    an_1, an = an, an * sign * xrad**2 / (counter * (counter - 1))
    counter += 2
    sign *= -1
	
print(f #format# ' SIN({x}) = {sinx}\nsin({x})={sin(xrad)}')	

