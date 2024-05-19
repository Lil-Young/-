# # 비밀번호 / D3

for tc in range(1, 11):
    a, num = input().split()
    pos = 0
    num = list(num)
    while pos < len(num)-1:
        if num[pos] == num[pos+1]:
            del num[pos:pos+2]
            pos-=1
            continue
        pos+=1
    print(f"#{tc} {''.join(num)}")