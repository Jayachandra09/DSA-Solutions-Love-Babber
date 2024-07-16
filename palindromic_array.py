def PalinArray(arr):
    # Code here
    count = 0
    for i in arr:
        remainder = 0
        reverse = 0
        temp = i 
        while(temp>0):
            remainder = temp%10
            reverse = reverse*10+remainder
            temp = temp//10
        if i == reverse:
            count+=1
    if count == len(arr):
        return True
    else:
        return False

# we can solve this by using string also we need to traverse from the back like str[::-1] ---if the string reverse is equal to string we can increse the count or we can directly return false in the else statement.

# Driver Code
arr = [111, 222, 333, 444, 555]
result = PalinArray(arr)
print(result)

# Problem link : https://www.geeksforgeeks.org/problems/palindromic-array-1587115620/1?page=1&sortBy=submissions
