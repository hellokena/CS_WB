# 그룹 단어 체커
# 접근 방법 : 전체를 그룹 단어로 가정하고, 그룹 단어 규칙에서 어긋나는 문자만큼 제외
def solution(words):
    answer = len(words) # 우선 전체를 그룹 단어라고 가정
    for word in words:
        for i in range(len(word)-1):
            if word[i] != word[i+1]: # 현재 위치와 다음 위치의 알파벳이 다르다면
                if word[i] in word[i+2:]: # 현재 위치의 알파벳이 뒤에도 있는가 확인 # word[i+1]은 어차피 다름 
                    answer -= 1 # 그룹 단어에서 제외
                    break ## 한번 이라도 그룹 단어가 아닐 경우, 뒤의 경우 확인하지 않아도 됨
    print(answer)

n = int(input())
words = []
for _ in range(n):
    words.append(input())
solution(words)
