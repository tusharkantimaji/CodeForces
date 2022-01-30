for _ in range(int(input())):
    n = int(input())
    s = input()
    for i in range(n):
        for j in range(i+1, n):
            p = s[i:j+1]
            if p == p[::-1]:
                print('NO')
                break
        else:
            continue
        break
    else:
        print('YES')

