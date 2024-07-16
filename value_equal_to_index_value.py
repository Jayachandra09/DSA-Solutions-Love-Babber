def EqualValue(arr):
  res = []
  for i in range(len(arr)):
    if i+1 == arr[i]:
      res.apppend(arr[i])
  return res

#Driver Code
arr = [15, 2, 45, 4 , 7]
result = EqualValue(arr)
print(result)

#Problem Link : https://www.geeksforgeeks.org/problems/value-equal-to-index-value1330/1?page=1&sprint=94ade6723438d94ecf0c00c3937dad55&sortBy=submissions
