# 회문2 / D3

for tc in range(1, 11):
    T = int(input())
    arr = []
    for _ in range(100):
        arr.append(list(input()))
    n_arr = []
    for i in range(100):
        a = []
        for j in range(100):
            a.append(arr[j][i])
        n_arr.append(a)
    re = 0
    start = 99
    for _ in range(100):
        for a, b in zip(arr, n_arr):
            for i in range(100):
                if i+start > 100:
                    break
                word1 = a[i:(i+start)]
                word2 = b[i:(i+start)]

                if word1 == list(reversed(word1)) or word2 == list(reversed(word2)):
                    if len(word1) > re:
                        re = len(word1)
        start-=1
                    
    print(f"#{T} {re}")