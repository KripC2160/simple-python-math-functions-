
###python code that finds value of term using recursive sequence###
"""
Warning: recursive formula is only good if you want to find the unknown value after known (e.g. n_35 -> n_36). 
If you want to find values that are not close to the known variables (e.g. n_35 -> n_205), then use the explicit-formula.py instead
"""
#original mathematical formula: a_n = a_(n-1) + d
# a is the value, n is the term, d is the difference 

def find_recursive(answer, difference):
    return answer + difference #yes, it's this simple 

print(find_recursive(known_answer, difference)) #replace a with the answer with term before the one you want to find, replace c for difference
