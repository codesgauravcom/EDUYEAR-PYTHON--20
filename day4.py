#print all the numbers divisible by 5and 7
for x in range(1,40):
    if x%5== 0 or x%7== 0:
        print(x)



    

# find the factorial of any number
num = 7
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


#take integer from user until he presses q,and print the sum of all numbers

total = 0
while True:
    a = input('enter a number or press to quit: ')
    if a == 'q':
        break
    total += int(a)
print("total",total)  


#find the sum of series
        
n=5
k=0       
l=[]
for i in range(1,n+1):
    s="2"*i
    l.append(s)
for i in range(len(l)):
    k+=int(l[i])
print(k)  

    

    




        