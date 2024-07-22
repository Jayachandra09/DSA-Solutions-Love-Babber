def longestCommonPrefix(self, n, arr):
    # code here
    min_str = arr[0]
    res_str = ""
    for i in range(1,len(arr)):
        if len(arr[i])<len(min_str):
            min_str = arr[i]
                
    for i in range(len(min_str)):
        count=0
        for j in range(len(arr)):
            if min_str[i]==arr[j][i]:
                count+=1
        if count == n:
            res_str+=min_str[i]
        
    if len(res_str)>0:
        return res_str
    else:
        return -1

#Driver code
arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
n = len(arr)
result = longestCommonPrefix(self, n, arr)
print(result)



