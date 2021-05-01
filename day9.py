'''Print following a pattern without using any loop. (Hint use recursive functions)

Example : 

Input: n = 16
Output: 16, 11, 6, 1, -4, 1, 6, 11, 16'''


def solve(a,b):
    print(a, end=' ')
    if a <= 0:
        return
    solve(a-b, b)    
    print(a, end=' ')

solve(10,5)
print()
solve(16,5)
print()
solve(12,3)
print()    