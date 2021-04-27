#all the index of vowels
vow_str = "eduyearclass"
new_vow = []
for ele in range(len(vow_str)):
    if vow_str[ele] in "aeiou":
       new_vow.append(ele)

print(str(new_vow))  

#reverse the string 
mystr = "eduyear is best"
res =  " ".join(reversed(mystr.split(" ")))
print("The string after reverse split : " + str(res))



#remove duplicate elements 
dup_list = [1,2,3,3,2,4]
print ("The original list is : " +  str(dup_list))
b = []
for i in dup_list:
    if i not in b:
        b.append(i) 
print ("The list after removing duplicates : " + str(b))
