l = [1,6,3,2,5,1,7]


def sum (a,b):
    return a + b
c = map(sum,l[:-1:2], l[1::2])
print (list(c))



l1 = l[::2]
l2 = l[1::2]
g = len(l1)
r = 0
while g > 0:
    a = l1[r]
    b = l2[r]
    c = sum(a,b)
    g -=1
    r +=1
    print(c)




l2 = [l[i] + l[i+1] for i in range(t-1)]
l3 = l2[::2]
print (l3)