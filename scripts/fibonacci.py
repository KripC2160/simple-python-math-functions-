

#fibonnaci sequence
#formula fn = fn-1 + fn-2

def fibonacci(forloop):
    bef, aft = 1
    for i in range(forloop):
        if i < 2:
            return 1
            print("1")
        else:
            res = bef + aft
            return res
            print(res)

fibonacci(forloop)
