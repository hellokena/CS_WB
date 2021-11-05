# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
answer = 0
for i in range(1, n+1):
	if n%i==0: answer += i
print(answer)
