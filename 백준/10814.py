n = int(input())
 
arr = []
for _ in range(n):
    age, name = input().split()
    arr.append([int(age),name])
arr.sort(key=lambda x:int(x[0]))
for i in arr:
    print(i[0],i[1])
    
# arr.sort(key=lambda x:int(x[0])
# -> x[0]은 age를 나타내는데 name은 신경끄고 age를 기준으로 정렬을 하는거임 그래서 입력받은 순서에서 나이만 신경쓰는거임