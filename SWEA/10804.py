# 문자열의 거울상 / D3

T = int(input())
for tc in range(1, T+1):
    s = input()
    word = ''
    for i in s:
        if i=='b': word+='d'
        elif i=='d': word+='b'
        elif i=='p': word+='q'
        elif i=='q': word+='p'
    word = ''.join((reversed(list(word))))
    print(f"#{tc} {word}")