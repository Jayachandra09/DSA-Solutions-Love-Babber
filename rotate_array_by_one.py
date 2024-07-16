def rotate(arr):
  temp1 = arr[-1]
  i = 0
  while(i<len(arr)-1):
    temp2 = arr[i+1]
    arr[i], arr[i+1] = temp1, arr[i]
    temp1 = temp2
    i+=2
  if len(arr)%2!=0:
    arr[-1] = temp
    return arr
  else:
    return arr
# this approach is used to traverse from the first 

  temp = arr[-1]
  for i in range(len(arr)-1, -1, -1):
    arr[i] = arr[i-1]
  arr[0] = temp
# this approach is used to traverse from the backside

#Driver code
arr = [1, 2, 3, 4, 5]
result = rotate(arr)
print(result)

#Problem Link : https://www.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1?page=1&sprint=94ade6723438d94ecf0c00c3937dad55&sortBy=submissions
