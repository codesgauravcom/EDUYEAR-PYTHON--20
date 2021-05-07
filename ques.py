#python program to map two lists into a dictionary
L1 = [1,2,3,4]
L2 = ['a','b','c','d']
d = dict(zip(L1,L2))
print(d)

# Write a Python program that accepts a string and calculate the number of digits and letter
s = input("Input a string")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)


#Write a Python function that takes a list of words and returns the length of the longest one.
def longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
result = longest_word(["Fullstack", "Interpreted", "Postgreesql"])
print("\nLongest word: ",result[1])
print("Length of the longest word: ",result[0])


#Write a Python program to construct the following pattern using a nested loop number
for i in range(6):
    print(str(i) * i)