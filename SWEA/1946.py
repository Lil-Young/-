# 간단한 압축 풀기 / D2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    alphabet = []
    for _ in range(N):
        a, n = map(str, input().split())
        for _ in range(int(n)):
            alphabet.append(a)
    print(f"#{tc}")
    for index, word in enumerate(alphabet):
        print(word, end='')
        if index%10 == 9:
            print()
    print()