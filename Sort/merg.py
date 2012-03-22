arr = [4,5,6,1,5,7]

ar2 = arr[len(arr)/2:]
ar1 = arr[:len(arr)/2]
print ar1, ar2


def A_to_aa(ar0):
    ar1 = []
    ar2 = []
    l = len(ar0)/2
    ar1 = ar0[:l]
    ar2 = ar0[l:]
    return ar1, ar2


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


print aa_to_A(ar1,ar2)
print arr
print aa_to_A(A_to_aa))



