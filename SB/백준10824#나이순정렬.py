import sys
n = int(sys.stdin.readline().rstrip()) # 회원 수
temp = []
for _ in range(n):
    age, name = sys.stdin.readline().rstrip().split()
    age = int(age) # 형변환
    temp.append([age,name])
temp.sort(key=lambda x:x[0]) # 나이로만 정렬
for x,y in temp:
    print(x, y)
