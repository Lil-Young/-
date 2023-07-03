R = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
S = str(input())
S = list(S)
list1 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
for i in range(len(S)) :
    for j in range (len(R)) :
        if S[i] == R[j] :
            if list1[j] == -1 :
                list1[j] = i
result = ' '.join(map(str, list1))
print(result)