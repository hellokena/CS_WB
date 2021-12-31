# 크로아티아 알파벳
def solution(s):
    alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    for a in alphabet:
        if a in s:
            s = s.replace(a, '.')
    print(len(s))
    
s = input()
solution(s)

# -----------------

# 크로아티아 알파벳
def solution(s):
    alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    for a in alphabet:
        s = s.replace(a, '.')
    print(len(s))

s = input()
solution(s)
