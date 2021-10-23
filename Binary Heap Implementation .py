#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Max Heap Implementation
# Time Complexity
# Inserting ELement :- O(Log(N))
# Deleting ELement :- O(Log(N))
# Finding Max ELement :- O(1)

# Space Complexity :- O(N)
# Auxillary Space of Recursion Stack

class binHeap:
    def __init__(self):
        self.heap=[]
        self.size=0
    # Inserting Element in Max Heap
    def insert(self,k):
        if self.size==0:
            self.heap.append(k)
            self.size+=1
        else:
            self.heap.append(k)
            self.size+=1
            i=self.size-1
            while i>0 and k>self.heap[i//2]:
                self.heap[i]=self.heap[i//2]
                i=i//2
            self.heap[i]=k
        
    # Finding Max Element 
    def findMaxElement(self):
        if self.size==0:
            return "Heap is Empty"
        return self.heap[0]
    
    # Reshuffling Max Heap in order to maintain the validity
    def heapify(self,indx):
        if indx>=self.size:
            return 
        maxiIndx=2*indx
        if maxiIndx<self.size-1 and self.heap[maxiIndx]<self.heap[maxiIndx+1]:
            maxiIndx+=1
        if self.heap[maxiIndx]<=self.heap[indx]:
            return
        self.heap[maxiIndx],self.heap[indx]=self.heap[maxiIndx],self.heap[indx]
        self.heapify(maxiIndx)
    
    # Removing the element from max heap, Max element is remove first        
    def remove(self):
        if self.size==0:
            return "Heap is Empty"
        maxiItem=self.heap[0]
        self.heap[0]=self.heap[-1]
        self.heap.pop(0)
        self.size-=1
        indx=self.size-1
        self.heapify(0)
        return maxiItem
        
        
        
obj=binHeap()
obj.insert(10)
obj.insert(0)
obj.insert(120)
obj.insert(-12)
obj.insert(90)
print(obj.remove())
print(obj.findMaxElement())


            
            
        
        

