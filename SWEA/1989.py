# 초심자의 회문 검사 / D2

T = int(input())
for test_case in range(1, T+1):
    s = list(input())
    temp = list(reversed(s))
    if s == temp:
        print(f"#{test_case} 1")
    else:
        print(f"#{test_case} 0")