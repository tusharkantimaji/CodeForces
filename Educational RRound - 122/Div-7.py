for _ in range(int(input())):
    n = int(input())
    if n % 7 == 0:
        print(n)
    else:
        p = str(n)
        p = p[:-1]
        left = int(p + str(1))
        right = int(p + str(9))
        for i in range(left, right+1):
            if i%7 == 0:
                print(i)
                break

