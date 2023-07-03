result = 10
word = list(map(str, input().rstrip()))
for i in range (len(word) - 1) :
    if word[i] == word[i+1] :
        result += 5
    else :
        result += 10
print(result)