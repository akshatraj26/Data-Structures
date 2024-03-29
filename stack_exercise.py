from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
        
    def push(self, x):
        return self.container.append(x)
    
    def pop(self):
        return self.container.pop()
    
    def isEmpty(self):
        return (self.container) == 0
    
    def peek(self):
        return self.container[-1]
    
    def size(self):
        return len(self.container)
    
    
        
def reverse_string(s):
        stack = Stack()
        
        for ch in s:
            stack.push(ch)
            
        rstr = ''
        while stack.size() != 0:
            rstr += stack.pop()
            
        return rstr    

def is_match(ch1, ch2):
    sign = {
        '}' : '{',
        ']': '[',
        ')' : '('
    }
    
    return sign[ch1] == ch2

def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch == '{' or ch == '[' or ch == '(':
            stack.push(ch)
            
        if ch == '}' or ch == ']' or ch == ')':
            if stack.size() == 0:
                return False
            if not is_match(ch, stack.pop()):
                return False
            
        return stack.size() == 0
    
    
            
# s = Stack()
# # s.push(45)
# # s.push('34fg')
# # s.push(34)
# # print(s.size())

# print(s.isEmpty())
# print(s.pop())  
# print(reverse_string('We will conquere COVID-19'))

if __name__ == '__main__':
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))