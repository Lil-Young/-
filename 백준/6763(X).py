import sys
input = sys.stdin.readline
a = int(input())
b = int(input())
if b-a >= 31: print(f"You are speeding and your fine is $500.")
elif b-a >= 21 and b-a <= 30: print(f"You are speeding and your fine is $270.")
elif b-a >= 1 and b-a <= 20: print(f"You are speeding and your fine is $100.")
else: print("Congratulations, you are within the speed limit!")

# https://www.acmicpc.net/problem/6763