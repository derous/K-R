a=[4, 13, 1, 12,9,18,5,16,7,10,14, 3, 11, 22,19,8,15,6,17,0]
#print a
iterat = 0
def read_data():
    return map(
        lambda s: int(s),
        open("QuickSort.txt", "r").readlines()) #"IntegerArray.txt"
a1 = read_data()
#print a

def Partition(a,n_p,n_home,n_end):
    print a[n_home:n_end], a[n_p]
    global iterat
    a[n_p], a[n_home] = a[n_home], a[n_p]
    a_p = a[n_home]
    i = n_home
    j = n_home
    #    print a[n_home:n_end]
    for a_i in a[n_home+1:n_end]:
        j += 1
        if a_i <= a_p:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i], a[n_home] = a[n_home], a[i]
    print a[n_home:n_end],a[i]
    iterat = iterat + j-n_home
    return i


def Quicksort(a,n_home,n_end):
    #n_p1 = n_home
    n_p1 = (n_home+(n_end-1))/2
    #n_p1 = n_end-1
    if n_home < n_end:
        r = Partition(a,n_p1,n_home,n_end)    #Insert element SORT 1=>(n_home), n=>(n_end-1), med=(n_home+(n_end-1))/2
        Quicksort(a,n_home,r)
        Quicksort(a,r+1,n_end)

p = 0
q = len(a)

Quicksort(a,p,q)
#print a
print iterat









