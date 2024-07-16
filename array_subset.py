from collections import Counter

def isSubset( a1, a2, n, m):
    # c1 = Counter(a1)
    # c2 = Counter(a2)
    # common = c1&c2
    # if common == c2:
    #     return "Yes"
    # else:
    #     return "No"
    
    for i in a2:
        if i in a1:
            a1.remove(i)
        else:
            return "No"
    return "Yes"
# when we use the Counter it will count hashable items (it will count duplicate values) and create a key and value pairs. 
# when we use the c1&c2 it will create a common keys and values from the both counters suppose 
#c1 = { 12: 2, 7: 1, 13: 2, 4: 3, 11: 1, 6: 3}
#c2 = {4: 2, 11: 1, 13:1}
# c1&c2 = {4: 2, 11: 1, 13:1} then if c1&c2 is equal to c2 then it a subset of c1

#Driver Code
a1 = [11, 7, 1, 13, 21, 3, 7, 3]
a2 = [11, 3, 7, 1, 7]
result = isSubset(a1, a2, n, m)
print(result)
