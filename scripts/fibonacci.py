

#fibonnaci sequence
#prints out e.g. 1,1,2,3,5,7,12
#formula fn = fn-1 + fn-2

def fibonacci(forloop):
    num = [0, 1] #array that holds the current and previous values
    for i in range(forloop):
        if i < 1:
            print(num[1])
        else:
            print(num[0]+num[1])
            num.append(num[0]+num[1])
            num.pop(0)

fibonacci(forloop) #replace for loops with amount value you want to get
