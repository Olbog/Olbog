def s (x,y):
    return x, y

a = list(map(int,input().split()))
for x in a[::2]:
    for y in a[1::2]:
        k = s(x,y)
        print(k)


