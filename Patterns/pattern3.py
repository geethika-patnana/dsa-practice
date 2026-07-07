# Right-Angled Triangle with Column Numbers

class Pattern3:
    def __init__(self,n):
        self.n = n

    def display(self):
        print("This is Pattern 3")
        for i in range(1,self.n+1):
            for j in range(1,i+1):
                print(j , end = " ")
            print()

n = int(input())
# Creating Object for the Class 
obj = Pattern3(n) 
obj.display()

'''
Time Complexity : O(n^2)
Space Complexity : O(1)

'''
'''
n = 3 

1
1 2
1 2 3

'''
