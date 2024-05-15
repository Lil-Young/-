# 죠교의 성적 매기기 / D2

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    student_grade = [None]
    for _ in range(N):
        a, b, c = list(map(int, input().split()))
        total = a*0.35 + b*0.45 + c*0.2
        student_grade.append(total)
    print(student_grade)