def PairsCount(arr, target):
  count = 0
  dic = {}
  for i in arr:
    if target-i in dic:
    # 
      count+=dic[target-i]
    if i in dic:
      dic[i]+=1
    else:
      dic[i]=1
  return count

# We can use for loop in for loop to solve this but the time complexity is n^2
count = 0
for i in range(len(arr)-1):
  for j in range(i, len(arr)):
    if arr[i]+arr[j]==target:
      c+=1
return count


#Driver code
arr = [1,5,7,1]
target = 6
result = PairsCount(arr, target)
print(result)

#Problem Link : https://www.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1
