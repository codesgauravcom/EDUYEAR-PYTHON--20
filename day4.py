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




n = int(input("Enter the numbers"))

sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i+1    
print("The sum is", sum)
    
        

    

    




        