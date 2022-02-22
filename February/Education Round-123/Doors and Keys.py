for _ in range(int(input())):
    s = input()
    p = []
    for i in s:
        if i == 'r':
            p.append(1)
        elif i == 'g':
            p.append(2)
        elif i == 'b':
            p.append(3)
        elif i == 'R':
            if 1 not in p:
                print('NO')
                break
        elif i == 'G':
            if 2 not in p:
                print('NO')
                break
        else:
            if 3 not in p:
                print('No')
                break
    else:
        print('YES')