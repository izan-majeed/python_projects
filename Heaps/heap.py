import math

class Heap():
    def __init__(self):
        self._A = [-math.inf]
        self.size = 0
        
        
    def insert(self, value):
        self._A.append(value)
        self.size += 1
        self._perup(value)
        print(f'{value} inserted!')
    
    def _perup(self, value):
        i = self.size
        parent_index = i//2
        
        while (parent_index > 0 and value < self._A[parent_index]):
            self._A[parent_index], self._A[i] = self._A[i], self._A[parent_index]
            parent_index //= 2
        
        
    def delete(self):
        if len(self._A)==1:
            print('Nothing to delete.')
            return
        root = self._A[1]
        self._A[1] = self._A[self.size]
        self._A.pop()
        self.size -= 1
        
        self._perdown(1)
        print(f'{root} deleted!')
    
    def _perdown(self,i):
        while (i*2 <= self.size):
            mc = self.minChild(i)
            
            if self._A[i] > self._A[mc]:
                temp = self._A[i]
                self._A[i] = self._A[mc]
                self._A[mc] = temp
                
            i = mc

    def minChild(self,i):
        if i*2 + 1 > self.size:
            return i * 2
        
        else:
            if self._A[i*2] < self._A[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
                    
                
    def display(self):
        print(self._A[1:])