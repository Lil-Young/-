from audioop import reverse

alp = list(map(str, input().rstrip()))
reverse_alp = list(reversed(alp))
alp = ''.join(alp); reverse_alp = ''.join(reverse_alp)
if alp == reverse_alp :
    print(1)
else :
    print(0)