def Firstprimes(n=2):
    for i in range(2, n+1):
        if n%i == 0:
            break
        return i  

def IsPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, n+1):
            if n%i == 0:
                return False
            else:
                return True  
def matches(s, t):
    l = 0
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                l +=1
    return l   

def characterCase(S):
    D = {}
    l = 0
    u = 0
    for item in S:
        if item.islower():
            l +=1
        if item.islower():
            u += 1
            
def sum_prod(n, m=1):
    A = 0
    B = 1
    for i in range(m, n+1):
        A +=i
        B *=i
    return A, B
print(sum_prod(10, 1))

def Facto(n):
    fact = 1
    for i in range(1,n+1):
        fact *=i
    return fact
print(Facto(57))

def ListComp(L):
    list1 = []
    list2 = []
    list3 = []
    for i in range(len(L)):
        list1.append(L[i])
    
        if len(L[i]) == len(L):
            list2.append(L[i])
        if len(L[i]) <=3:
            list3.append(L[i])
            
    for item in list1:
        list1.remove(list1[-1])
    return list1.pop(), list2, list3

def V(n, p):
    for i in range(n):
        if n%(p**r) == 0:
            return r
print(V(40, 2))        
    
    