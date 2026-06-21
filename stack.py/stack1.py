class Stack:
    def __init__(self):
         self.st=[]
    def push(self,value):
        self.value=value
        self.st.append(value)
        print(self.st)
#      def is_empty(self):
#            if len(self.st)==0:
#               print()
    def pop(self):
          print(self.st.pop())
          print(self.st)
#         if not self.is_empty():
#              self.st.pop()
#         else:
#              print(-1)
    def peek(self):
       if self.st is None:
           print("empty")
       else:
           print(self.st[-1])
    def empty(self):
        if len(self.st)==0:
           print("Stack is empty") 
        else:
           print("stack have elements")                      
        
stack=Stack()
stack.push(10)
stack.push(8)
stack.pop()
stack.push(1)
stack.peek()
stack.empty()

