n = int(input())
clap = 0
for num in range(n):
	for i in str(num):
		if int(i) in [3,6,9]: clap += 1
print(clap)
