# 두 단어가 다른 알파벳 갯수가 몇개있는지 확인
def check(str1, str2):
    tmp = 0
    for s1, s2 in zip(str1, str2):
        if s1 != s2: 
            tmp += 1
    return tmp
        
def solution(begin, target, words):
    answer = 0
    if target not in words: # 만약 바꾸고자 하는 단어가 없으면 못만듬
        return 0
    
    while begin != target:
        # words안에 있는 단어 중 한 개의 알파벳만 다른 단어를 찾는다
        replace = [word for word in words if check(begin,word)==1]
        
        # case 1 : 바꿀 수 있는 단어가 없는 경우
        if not replace: # begin과 target이 같지 않은데 바꿀 수 없는 단어가 없다면(replace가 비어있음)
            return 0 # 바꿀 수 없는 경우
        
        # case 2 : 바꿀 수 있는 단어가 여러개인 경우
        if len(replace) > 1: #바꿀 수 있는 단어가 여러개인경우 target과 더 비슷한것 고름
            replace.sort(key=lambda x:check(target,x)) # check 함수의 반환값이 작을 수록 / 다른 알파벳 갯수의 갯수가 적을 수록 target과 가까운 것
            
        # replace가 하나라도 있을 경우   
        begin = replace[0] # 시작 단어 다시 초기화
        words.remove(begin) # 한번 사용한 것 지우기
        answer += 1 # 한번 변경했으니 카운트
    return answer
