# 다솔이의 다이아몬드 장식 / D3

T = int(input())
for tc in range(1, T+1):
    s = input()
    a = '...#'*len(s); a+='..'
    b = '.#'*(len(s)*2); b+='.'
    c = '#'
    for i in s:
        c+=('.' + i + '.#')
    print(a[1:])
    print(b)
    print(c)
    print(b)
    print(a[1:])