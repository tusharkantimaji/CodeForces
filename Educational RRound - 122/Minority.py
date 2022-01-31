for _ in range(int(input())):
    n = input()
    if len(n) <= 1:
        print(0)
    elif n == '01' or n == '10':
        print(0)
    else:
        c_0 = 0
        c_1 = 0
        for i in n:
            if i == '0':
                c_0 += 1
            else:
                c_1 += 1
        if c_0 == c_1:
            print((len(n)-1)//2)
        else:
            print(min(c_0, c_1))
