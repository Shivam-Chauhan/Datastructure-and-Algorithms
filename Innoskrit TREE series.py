#!/usr/bin/env python
# coding: utf-8

# In[5]:


class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self):
        self.root=None
        
    # Preorder Traversal
    def preorder(self,root):
        if root!=None:
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
        else:
            return
    # Inorder Traversal
    def inorder(self,root):
        if root is None: return
        self.inorder(root.left)
        print(root.data,end=" ")
        self.inorder(root.right)
    
    # Postorder Traversal
    def postorder(self,root):
        if root is None: return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data,end=" ")
        
    def nodeCounter(self,root):
        if root is None: return 0
        
        return 1+ self.nodeCounter(root.left) + self.nodeCounter(root.right)
    
    def leafCount(self,root):
        if root is None : return 0
        elif root.left==None and root.right==None: return 1
        return self.leafCount(root.left) + self.leafCount(root.right)
    
    def nonLeafCount(self,root):
        return self.nodeCounter(root)-self.leafCount(root)
    
    def countOfFullNodes(self,root):
        if root is None : return 0
        elif root.left==None or root.right==None: return 0
        elif root.left!=None and root.right!=None: return 1+ self.countOfFullNodes(root.left) + self.countOfFullNodes(root.right)
    
    def bfsTraversal(self,root):
        queue=[]
        queue.append(root)
        while queue:
            rem=queue.pop(0)
            print(rem.data,end=" ")
            if rem.left!=None: queue.append(rem.left)
            if rem.right!=None: queue.append(rem.right)
    
    def zigzagTraversal(self,root):
        queue=[]
        storage={}
        queue.append((root,0))  # Node and Level
        while queue:
            rem,level=queue.pop(0)
            if level not in storage.keys(): storage[level]=[rem.data]
            else: storage[level].append(rem.data)
            
            if rem.left!=None: queue.append((rem.left,level+1))
            if rem.right!=None: queue.append((rem.right,level+1))
        
        # Printing values in ZigZag Fashion
        for key,val in storage.items():
            if key&1: print(val[::-1])
            else: print(val)
    
    def levelSuccessor(self,root,key):
        queue=[]
        queue.append(root)
        while queue:
            rem=queue.pop(0)
            if rem.data==key: print("Level Successor is :- ",queue[0].data)
                
            if rem.left!=None: queue.append(rem.left)
            if rem.right!=None: queue.append(rem.right)
                
    def minDepth(self,root):
        queue=[]
        queue.append((root,1)) # Node and it's height
        while queue:
            rem,level=queue.pop(0)
            if rem.left==None and rem.right==None:
                print("Min Depth of the tree is :- ", level)
                break
            
            if rem.left!=None: queue.append((rem.left,level+1))
            if rem.right!=None: queue.append((rem.right,level+1))
    
    def rightView(self,root):
        queue=[]
        queue.append((root,0)) # Node and it's level
        output=[]
        while queue:
            rem,level=queue.pop(0)
            if len(queue)==0: output.append(rem.data)
            elif level+1==queue[0][1]: output.append(rem.data)
            
            if rem.left!=None: queue.append((rem.left,level+1))
            if rem.right!=None: queue.append((rem.right,level+1))
                
        print(output)  # Right View of Binary Tree
    
    def pathSum(self,root,key,summation):
        if root==None: return False
        if summation==key: return True
        if root:
            return self.pathSum(root.left,key,summation+root.data) or self.pathSum(root.right,key,summation+root.data)
    
    def sumRootLeaf(self,root,summation):
        if root.left==None and root.right==None:
            return int(summation+str(root.data))
        elif root:
            return self.sumRootLeaf(root.left,summation+str(root.data)) + self.sumRootLeaf(root.right,summation+str(root.data))
    
    
    def issequence(self,root,array,counter):
        if root.left==None and root.right==None:
            if len(array)==counter+1 and array[counter]==root.data: return True
            return False
        if root:
            return self.issequence(root.left,array,counter+1) or self.issequence(root.right,array,counter+1) 
    def diameterBTree(self,root):
            if root==None: return 0
            left_height=self.diameterBTree(root.left)
            right_height=self.diameterBTree(root.right)
            self.res=max(self.res,left_height+right_height)
            return 1+max(left_height,right_height)
    
    def LCA(self,root,p,q):
            if root==None: return None
            if root.data==p.data or root.data==q.data: return root
            leftChild=self.LCA(root.left,p,q)
            rightChild=self.LCA(root.right,p,q)
            
            if leftChild is not None and rightChild is not None: return root
            
            
            return leftChild if leftChild is not None else rightChild
    
    def mergeBTree(self,root1,root2):
        if root1 is None: return root2
        if root2 is None: return root1
        
        root1.data+=root2.data
        root1.left=self.mergeBTree(root1.left,root2.left)
        root2.left=self.mergeBTree(root1.right,root2.right)
        return root1
    
    def issymmetric(self,root1,root2):
        if root1==None and root2==None: return True
        if root1==None or root2==None: return False
        
        return (root1.data==root2.data) and (self.issymmetric(root1.left,root2.right)) and (self.issymmetric(root1.right,root2.left))
        
        
            
            
    
tree=BinaryTree()
tree.root=Node(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)
tree.root.right.left=Node(6)
tree.root.right.right=Node(7)
# tree.preorder(tree.root)
# print()
# tree.inorder(tree.root)
# print()
# tree.postorder(tree.root)
# print()
# nodeCount=0
# print(tree.nodeCounter(tree.root))
# print(tree.leafCount(tree.root))
# print(tree.nonLeafCount(tree.root))
# print(tree.countOfFullNodes(tree.root))
# tree.bfsTraversal(tree.root)
# tree.zigzagTraversal(tree.root)
# tree.levelSuccessor(tree.root,3)
# tree.minDepth(tree.root)
# tree.rightView(tree.root)
# key=100
# print(tree.pathSum(tree.root,key,0))
# print(tree.sumRootLeaf(tree.root,""))
# print(tree.issequence(tree.root,[1,2,4],0))
# tree.res=-10**9
# tree.diameterBTree(tree.root)
# print(tree.res)
# print(tree.LCA(tree.root,tree.root,tree.root.right.right).data)
# tree.mergeBTree(tree.root1,tree.root2)
# tree.issymmetric(tree.root,tree.root)

