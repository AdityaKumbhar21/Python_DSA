# Implementing Stack using list

class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, val):
        self.items.append(val)
    
    def size(self):
        return len(self.items)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")
    





stack_1 = Stack()
print(stack_1.is_empty())  #will return true if stack is empty else false

stack_1.push(10)
stack_1.push(200)
stack_1.push(301)

print(stack_1.is_empty())  #will return true if stack is empty else false

print(stack_1.peek())  #will print the top element of the stack

print(stack_1.pop())  # will remove the top element and return it
print(stack_1.peek())  #will print the top element of the stack





