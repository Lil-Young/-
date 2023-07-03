import sys
input = sys.stdin.readline
val_list = ["0o"]
val = input().strip("\n")
val_list.append(val)
val_total = (val_list[0]+val_list[1]) # 입력한 문자 앞에 8진수를 나타내는 0o 추가
val_10 = int(val_total, 8) # 문자열 8진수를 10진수로 변환
val_2 = bin(val_10) # 10진수 -> 2진수
print(val_2[2:])

