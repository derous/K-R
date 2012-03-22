a = [4,4,4,2]
print a

def A_LR(a):
    r = 0
    l = 0
    L_a = len(a)-1
    a_o = a[(L_a)/2]
    b = a
    print 'a_cp[',L_a/2,'] <',a_o
    for ai in a:
        if ai >= a_o:
            b[L_a-r] = ai
            r = r + 1
        else:
            b[l] = ai
            l = l + 1
    return b[:l],b[l:]
b=A_LR(a)
print b, 'mas1=', b[0], 'mas2=', b[1]

b=A_LR(b[0])
print b, 'mas1=', b[0], 'mas2=', b[1]

b=A_LR(b[0])
print b, 'mas1=', b[0], 'mas2=', b[1]

def A_to_LR(a):
    l = 0
    r = len(a)-1
    a_o = a[r/2]
    while l < r:
        tmp = a[l]
        a[l] = a[r]
        a[r] = tmp
        while  a[l] < a_o and l < r:
            l = l+1
            while a[r] >= a_o and l <= r:
                r = r-1
    return a[:l],a[l:]

print a
#t=A_to_LR(a)
#print A_to_LR(a)
#print t





