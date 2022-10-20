import random 
n = int(input("Enter n = "))
list = []
for i in range(n):
	x = random.randint(0, 100)
	list.append(x)
print(list)
sum = sum(list)
ave = sum / len(list)
print("The sum is:", sum)
print("The average is:", ave)

#list.insert(position in list, element in list) - adds elements in list in an exact position
