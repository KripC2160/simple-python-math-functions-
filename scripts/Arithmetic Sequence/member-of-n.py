
#this is a code that can check if the number is a member of the sequence
#formula: num = d(n-1)+ n_1


def is_member(num, diff, n1):
    if (num - n1) % 2 == 0: #Checks if number is an interger or float 
        return ((num - diff) / n1) + 1
        find_n(num, n1, diff)
    else: 
        return False

def find_n(num, n1, diff):
    while n1 < num:
        n1 += diff

    if n1 >= num:
        return n1    
        print(n1)

print(is_member(56, 2, 2))