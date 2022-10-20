shape = int(input('Choose shape (1 for square, 2 for triangre or 3 for trapezoid):'))

if shape == 1:
	a = int(input('Enter side:'))
	print('S =',a**2)
elif shape == 2:
	a = int(input('Enter side:'))
	h = int(input('Enter height:'))
	print('S =',a * h / 2)
elif shape == 3:
	a = int(input('Enter first base:'))
	b = int(input('Enter second base:'))
	h = int(input('Enter height:'))
	print('S =',(a+b) * h / 2)
else:
	print('Enter valid integer!')
