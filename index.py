## COUTNTDOWN
def cdown(num):
    clist= []
    for num in range(num,0,-1):
        clist.append(num)
    return clist

x= cdown(20)
print(x)

##PRINT & RETURN
def p_r(listvar):
    print(listvar[0])
    return(listvar[1])
list1= [6,0]
y= p_r(list1)
print(y)

##First plus length
def first_plus(listplus):
    return(listplus[0] + len(listplus))

list2=[10,5,3,4,6]
z= first_plus(list2)
print (z)

## valuess greater than second
def greater_sec(oglist):
    newlist= []
    for t in oglist:
        if t>oglist[1]:
            newlist.append(t)
    if len(newlist) <2:
        return False
    else: 
        return newlist
testlist = [5,3,6,8,9,1,2,5]
lowlist = [1,3,4,1,2]
q = greater_sec(testlist)
print(q)
w = greater_sec(lowlist)
print(w)

## this length that value
def le_va(v= 10,l=10):
    thelist=[]
    thelist.append(f"{v}," * l)
    return(thelist)
p= le_va(30,40)
print(p)
