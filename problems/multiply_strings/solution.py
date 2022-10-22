class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        real1 = 0
        place = 1
        while num1:
            real1 += int(num1[-1])*place
            place *= 10
            num1 = num1[:-1]
            
        real2 = 0
        place = 1
        while num2:
            real2 += int(num2[-1])*place
            place *= 10
            num2 = num2[:-1]
        
        return str(real1*real2)