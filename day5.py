#check whether the whole list is palindrome or not
list1 = [1,2,1]
list2= [1,2,2]
if list1== list1[::-1]:
    print("palindrome")

    if list2!= list2[::-1]:
        print("not palindrome")



#count even numbers and odd numbers
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
even_count , odd_count  = 0,0
for x in list1:
    if x%2==0:
        even_count += 1
    else:
        odd_count += 1
print(even_count)
print(odd_count) 


#print the numbers which are palindrome inside the list
mylist =[121,4334,876,987,5555]
for items in mylist:
    if int(items)== mylist[::-1]:
        print(items)








    

    



 