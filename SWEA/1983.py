# 죠교의 성적 매기기 / D2

grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

T = int(input())
for test_case in range(1, T+1):
    n, k = map(int, input().split())
    arr = []

    for i in range(n):
        a, b, c = map(int, input().split())
        score = a*0.35 + b*0.45 + c*0.2
        arr.append(score)

    target = arr[k-1]
    arr.sort(reverse=True)
    rate = n//10
    ratio_score = arr.index(target) // rate
    print(f"#{test_case} {grades[ratio_score]}")