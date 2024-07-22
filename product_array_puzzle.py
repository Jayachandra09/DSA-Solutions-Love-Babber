def productExceptSelf(nums, n):
    #1st Approach
    res = []
    c = 0
    prdct = 1
    for i in nums:
        if i==0:
            c+=1
        else:
            prdct*=i
        
    for i in range(len(nums)):
        if c>1:
            res.append(0)
        elif c==0:
            res.append(prdct//nums[i])
        elif c==1 and nums[i]!=0:
            res.append(0)
        else:
            res.append(prdct)
    return res

  #2nd Approach
    arr = [1]*n
    pre_prdct = 1
    post_prdct =1
    for i in range(n):
        arr[i]*=pre_prdct
        pre_prdct*=nums[i]
    for i in range(n-1,-1,-1):
        arr[i]*=post_prdct
        post_prdct*=nums[i]
    return arr


#Driver Code
nums = [10, 3, 5, 6, 2]
n = len(nums)
result = productExceptSelf(nums, n)
print(result)

#Problem Link : https://www.geeksforgeeks.org/problems/product-array-puzzle4525/1
