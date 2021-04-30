#program to print factorial
def fact(n):
    if n==0:
        return 1

    else:
        return n * fact(n-1) 
n= int(input("input a number :"))
print(fact(n))           

#To check the number  whether it is prime or not !
num=7
flag=0
for i in range(2,num):
    if num%i ==0:
        flag =1
        break
if flag ==1:
    print("not a prime number")
else:
    print("prime number")                 