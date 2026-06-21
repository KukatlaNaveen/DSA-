# use stack to reverse string
def string(s):
    st=[]
    for ch in s:
       st.append(ch)
    print(st)
    reverse=""
    while st:
         reverse+=st.pop()
    print(reverse)
string("soft")

# check if parentheses are balanced in a string
# implement min stack
class Min_Stack:
      def __init__(self):
          self.stack=[]
          self.min=[]
      def push(self,ele):
         self.stack.append(ele)
         if not self.min or ele<=self.min[-1]:
             self.min.append(ele)
      def all(self):
           for i in range(len(self.stack)):
               print(self.stack[i],end=" ")
#                print(self.min[i])
      def get_min(self):
          if self.min:
             print("\n",self.min[-1])
st=Min_Stack()
st.push(5)
st.push(4)
st.push(3)
st.push(2)
st.push(1)
st.all()
st.get_min()
                        
