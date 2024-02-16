"""
Write a program that implements a stack data structures of specified size. If the stack becomes full and we try to push an
element to it, then an IndexError exception should be raised. Similarly, if the stack is empty and we try to pop an
element from it then an IndexError exception should be raised.

"""

class Stack:
    def __init__(self, size):
        self.size = size
        self.arr = []
        self.top = -1
    
    def isFull(self):
        return True if self.top +1 == self.size else False   
    
    def isEmpty(self):
        return True if self.top == -1 else False
    
    def push(self, n):
        if self.isFull():
            raise IndexError("Stack is full")
        else:
            self.top += 1
            self.arr = self.arr + [n]
    
    # pop is not working properly
    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        else:
            n = self.arr[self.top]
            self.arr.pop()
            self.top = self.top - 1
            
            return n
        
    def printall(self):
        print(self.arr)
        
    def peek(self):
        print(self.arr[self.top])

# try:       
#     s = Stack(5)
#     s.push(34)
#     s.push(54)
#     s.push(23)
#     s.push(56)
#     s.push(78)
#     s.peek()
#     s.printall()
#     s.pop()
#     s.push(546)
#     s.printall()
    
# except Exception as e:
#     print(e.args)

s = Stack(5)
try:
    s.push(10)
    s.push(56)
    s.push(45)
    s.push(78)
    s.printall()
    print("Pop value",s.pop())
    
    # n = s.pop()
    print("after pop")
    s.printall()
    # s.push(20)
    # s.push(30)
    # s.push(40)
    # s.push(50)
    # # s.push(60)
    # s.printall()
    # s.peek()
    # s.push(70)
    
    
except Exception as e:
    print(e.args)
    
# print(dir(s))


        