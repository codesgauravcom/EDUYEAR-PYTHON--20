#program to print factorial
def fact(n):
    if n==0:
        return 1

    else:
        return n * fact(n-1) 
n= int(input("input a number :"))
print(fact(n))           

#To check the number  whether it is prime or not !
def prim(n):
    if(n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if (n % x==0):
                return False
            return True
    print(prim(3))                   