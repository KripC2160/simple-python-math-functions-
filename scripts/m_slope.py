
#this function finds slope of a line 

def m_slope(x1, y1, x2, y2):
    result1 = str(y2-y1)+'/'+str(x2-x1)
    result2 = (y2-y1)/(x2-x1)
    return result1, result2

result1, result2 = m_slope(x1, y1, x2, y2) #replace the values with the values of two points for slope
print(result1,'\n',result2)