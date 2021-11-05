# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
if n == 1: print(False) # 1은 소수가 아님
else:
	for i in range(2, int(n**0.5)+1): # 제곱근 사용
		if n % i == 0: # 나누어지면 
			print(False) # 소수가 아님
			break 
	else: print(True) # for-else문 : for문 안에서 break가 발생하지 않았을 때 실행됨
