# # 암호문3 / D3

for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    c = int(input())
    command = list(input().split())
    a=[]
    while command:
        cmd = command.pop(0)
        if cmd == 'I':
            x, y = int(command.pop(0)), int(command.pop(0))
            for _ in range(y):
                v = int(command.pop(0))
                arr.insert(x, v)
                x+=1
        elif cmd == "D":
            x, y = int(command.pop(0)), int(command.pop(0))
            del arr[x:x+y]
        elif cmd == "A":
            y = int(command.pop(0))
            for _ in range(y):
                v = int(command.pop(0))
                arr.append(v)
    result = arr[:10]
    print(f"#{tc}", end=' ')
    for i in result:
        print(f"{i}", end=' ')
    print()