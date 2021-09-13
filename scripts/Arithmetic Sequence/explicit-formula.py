
###python code that finds value of term using explicit formula###

#original mathematical formula: a_n = a_1 + d(n-1)
# a is the value, n is the term, d is the difference 

def find_diff(n1, diff, val):
    for i in range (val - 1):
        n1 += diff
    return n1

print(find_diff(a, b, c)) #replace a with the n_1, b with difference, c with value you want to get 

