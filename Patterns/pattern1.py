class Pattern1:
    def __init__(self,n):
        self.n = n

    def display(self):
        print("This is Pattern 1")
        for i in range(n):
            print("* " * n)

n = int(input())
# Creating Object for the Class 
obj = Pattern1(n) 
obj.display()

'''
Time Complexity : O(n)
Space Complexity : O(1)

'''
'''
n = 3 

* * *
* * *
* * *

'''
