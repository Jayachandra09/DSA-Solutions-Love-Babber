def Maximize(arr):
  arr.sort()
  sum_arr = 0
  mod = (10**9)+7
  for i in range(len(arr)):
    sum_arr = (sum_arr+arr[i]*i)%mod
  return sum_arr

#Driver Code
arr = [5, 3, 2, 4, 1] #Output - 40
result = Maximize(arr)
print(result)

#Problem Link : https://www.geeksforgeeks.org/problems/maximize-arrii-of-an-array0026/1
