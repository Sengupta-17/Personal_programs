class Solution:

    def kthSmallest(self, arr,k):
        
        for i in range(0,k-1):
            x=min(arr)
            arr.remove(x)
        x=min(arr)
        return x