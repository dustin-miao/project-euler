with open('answer.txt', 'w+') as af:
	print(sum([i for i in range(101)]) ** 2 - sum([i * i for i in range(101)]), file = af)