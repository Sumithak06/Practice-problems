pal = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        a = i*j
        copy = a
        rev = 0
        while (a != 0):
            rem = a % 10
            rev = rev * 10 + rem
            a = a // 10
        if(copy == rev) and (rev > pal):
            pal = rev
print(pal)