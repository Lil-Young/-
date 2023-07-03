def self_num () :
    a = range(1, 10000, 1)
    arr = list(a)
    self_num, n = 1, 0
    for i in range(9999) : # i는 인덱스값
        if i < 9 :
            n+=1
            self_num = n
            self_num += self_num             
            arr.remove(self_num)
        elif i < 99 :
            n+=1
            self_num = n
            self_num2 = list(map(int, str(self_num)))
            self_num2 = self_num + self_num2[0] + self_num2[1]
            if self_num2 > 10000 or self_num2 not in arr:
                pass
            else : 
                arr.remove(self_num2)
        elif i < 999 :
            n+=1
            self_num = n
            self_num2 = list(map(int, str(self_num)))
            self_num2 = self_num + self_num2[0] + self_num2[1] + self_num2[2]
            if self_num2 > 10000 or self_num2 not in arr:
                pass
            else : 
                arr.remove(self_num2)
        elif i < 9999 :
            n+=1
            self_num = n
            self_num2 = list(map(int, str(self_num)))
            self_num2 = self_num + self_num2[0] + self_num2[1] + self_num2[2] + self_num2[3]
            if self_num2 > 10000 or self_num2 not in arr:
                pass
            else : 
                arr.remove(self_num2)
    return arr
result = self_num()
for i in range (len(result)) :
    print(result[i])