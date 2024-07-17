class MyQueue:
    
    def __init__(self):
        self.arr = []
    
    #Function to push an element x in a queue.
    def push(self, x):        
         #add code here
        self.arr.append(x)
        return self.arr
 
  #Function to pop an element from queue and return that element.
    def pop(self):          
         # add code here
        if len(self.arr)==0:
            return -1
        element = self.arr.pop(0)
        return element

#Problem Link : https://www.geeksforgeeks.org/problems/implement-queue-using-array/1
