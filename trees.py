#Q1 — Maximum Depth of Binary Tree
# Find the maximum depth (height) of a binary tree.

# Input:
#         1
#        / \
#       2   3
#      / \
#     4   5

# Output: Maximum depth is 3
from collections import deque
class Tree:
 def __init__(self,value):
     self.value=value
     self.left=None
     self.right=None  
root=Tree(10)
root.left=Tree(8)
root.right=Tree(6)
root.right.right=Tree(4)
root.right.left=Tree(2)
def tree_height(root):
    if not root:
       return 0
    queue=deque([root])
    depth=0
    while queue:
       for i in range(len(queue)):
           node=queue.popleft()
         #   print(node.value,end=" ")
           if node.left:
              queue.append(node.left)
           if node.right:
              queue.append(node.right)
       depth+=1
    print("maximum depth is :",depth)
tree_height(root)
        