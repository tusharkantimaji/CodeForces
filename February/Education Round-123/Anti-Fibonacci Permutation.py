for _ in range(int(input())):
    n = int(input())
    for i in range(1, n+1):
        idx = n
        for j in range(0, i-1):
            print(idx, end=" ")
            idx -= 1
        print(1, end=" ")
        for j in range(0, n-i):
            print(idx, end=" ")
            idx -= 1
        print()