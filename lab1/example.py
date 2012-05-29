str=r'c:\newtext'
str1='c:\new\text\\'
print str
print str1


a = int('101',2)
b = pow(a,2)
c = round(2.5)
print(a,b,c)
d =0.1*3-0.3
print(d)
d = set('asd')
d1 = set('aesd')
d.remove('a')
print(d,d|d1)

L = {1,2,3,4,'qw'}
L1 = {'adg'}

print(L,L|L1,L1)

L1 = [1,2,3,4,5,6,7]
L2 = [1,3,6]
Ls1=set(L1)
Ls2 = set(L2)
Ls2
print(Ls1,'-',Ls2,'=',Ls1-Ls2)
print(Ls1,list(Ls2))
Ls2.add(1)
a=1
print(Ls2)