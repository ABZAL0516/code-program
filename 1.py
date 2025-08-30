class Stack:
   def __init__(self,capacity):
       self.stack = []
       self.capacity = capacity

   def push(self,value):
       if len (self.stack)>= self.capacity:
           print("Stack Overflow ! cannot push",value)
       else:
           self.stack.append(value)
           print(value,"pushed into Stack .")
   def pop(self):
       if not self.stack:
           print("Stack underflow! is empty.")
           return None
       else:
           return self.stack.pop()
   def peek(self):
       if not self.stack:
           print("Stack is empty.")
           return None
       else:
           return self.stack[-1]
   def display(self):
       if not self.stack:
           print("Stack underflow ! stack  is empty .")
       else:
           print("Stack elements:",self.stack)

s=Stack(5)
s.push(10)
s.push(20)
s.push(30)
s.display()

print("Top element:",s.peek())
print("popped:",s.peek())
s.display()