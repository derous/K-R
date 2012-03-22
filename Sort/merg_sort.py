a = [5,4,3,4,7,87,6,-9]

def aa_to_A(ar1, ar2):
    arr0=[]
    while len(ar1) + len(ar2) >0:
        if len(ar1) == 0:
            arr0 = arr0 + ar2[:1]
            ar2 = ar2[1:]
        else:
            if len(ar2) == 0:
                arr0 = arr0 + ar1[:1]
                ar1 = ar1[1:]
            else:
                if ar1[0]<ar2[0] :
                    arr0 = arr0 + ar1[:1]
                    ar1 = ar1[1:]
                else:
                    arr0 = arr0 + ar2[:1]
                    ar2 = ar2[1:]
    return arr0

def A_to_aa(ar0):
    l = len(ar0)/2
    ar1 = ar0[:l]
    ar2 = ar0[l:]
    if len(ar1)>1:
        t=A_to_aa(ar1)
        a1 = aa_to_A(t[0],t[1])
    else:
        a1 = ar1
    if len(ar2)>1:
        t=A_to_aa(ar2)
        a2 = aa_to_A(t[0],t[1])
    else:
        a2 = ar2
    return a1, a2

def MergSort(a):
    t=A_to_aa(a)
    return aa_to_A(t[0],t[1])

print MergSort(a)