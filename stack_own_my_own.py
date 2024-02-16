class Stack:
    def __init__(self, size):
        self.size = size
        self.arr = []
        self.top = -1
        
    def push(self, n):
        if self.top +1 == self.size:
            raise IndexError("Stack is full")
        else:
            self.top += 1
            self.arr +=  [n]
            
    def peek(self):
        if self.isEmpty():
            raise IndexError("Stack is Empty")
        else:
            return self.arr[self.top]
            
    def pop(self):
        if self.top == -1:
            raise IndexError("Stack is Empty")
        else:
            n = self.arr[self.top]
            # self.arr[self.top] = None
            
            # After comenting bottom line peek value is returing right value
            # self.top =self.top - 1
            return n
            # return self.arr.pop()
        
    
            
    def isEmpty(self):
        if self.top ==-1:
            return True
        else:
            return False
    
    def isFull(self):
        if self.top + 1  == self.size:
            print("I am overflowing")
        else:
            print("I can still take it.")
              
    
        
    def printall(self):
        print(self.arr)
            
s = Stack(5)
s.push(4)
s.push(56)
s.push(45)
s.push(34)
s.push(787)
s.printall()
# s.isEmpty()
# s.isFull()

s.pop()
s.pop()
s.printall()
print(s.peek())
try:
    s.push(67)
except Exception as e:
    print(e.args)
        