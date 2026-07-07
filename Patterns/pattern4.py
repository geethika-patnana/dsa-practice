#Right-angled Number Triangle

class Pattern4:
    def __init__(self,n):
        self.n = n

    def display(self):
        print("This is Pattern 4")
        for i in range(1,self.n+1):
            for j in range(i):
                print(i , end = " ")
            print()

n = int(input())
# Creating Object for the Class 
obj = Pattern4(n) 
obj.display()

'''
Time Complexity : O(n^2)
Space Complexity : O(1)

'''
'''
n = 3 

1
2 2
3 3 3

'''
