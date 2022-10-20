list = [1, 2, 3, 4, 5]
print(list)
k = 1
for i in range(len(list) - 1):
	sum = int(list[i+i]+list[i+k])
	list.insert(i+k, sum)
	k+=1
print(list)

