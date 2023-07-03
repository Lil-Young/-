word = input().upper()
dic = {}
for i in set(word) :
    dic[i] = word.count(i)
max_cnt = max(dic.values())
val_list = list(dic.values())
if val_list.count(max_cnt) > 1:
    print("?")
else :
    reverse_dic = dict(map(reversed, dic.items()))
    print(reverse_dic.get(max_cnt))