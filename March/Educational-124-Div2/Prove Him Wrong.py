import sys
for _ in range(int(input())):
    n = int(input())
    arr = []
    p = 1
    for i in range(n):
        arr.append(p)
        p = 3*p + 1
        if p > sys.maxsize:
            print('NO')
            break
    else:
        print('YES')
        for i in arr:
            print(i, end=" ")
        print()