class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        numsets = []
        products = set()

        s = []
        for num in nums:
            if num == 0:
                if s:
                    numsets.append(s)
                products.add(0)
                s = []
            else:
                s.append(num)
        if s:
            numsets.append(s)
        
        
        def findProducts(nums):
            curproducts = set()
            prev = 1
            for n in nums:
                prev *= n
                curproducts.add(prev)
            products.add(max(curproducts))
            for i in range(1, len(nums)):
                curproducts = set([s//nums[i-1] for s in curproducts])
                products.add(max(curproducts))
                
            
            
            
        for numset in numsets:
            findProducts(numset)
        
        return max(products)
        
        
        
    
                
        