class Pattern2:
    def __init__(self,n):
        self.n = n

    def display(self):
        print("This is Pattern 2")
        for i in range(n+1):
            print("* " * i)

n = int(input())
# Creating Object for the Class 
obj = Pattern2(n) 
obj.display()

'''
Time Complexity : O(n)
Space Complexity : O(1)

'''
'''
n = 3 

* 
* * 
* * *

'''
