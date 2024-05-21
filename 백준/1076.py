a = input()
b = input()
c = input()

arr = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
print(int(str(arr.index(a)) + str(arr.index(b))) * 10**arr.index(c))