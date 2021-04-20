class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        num = str(n)
        sum = 0
        product = 1
        for c in num:
            c= int(c)
            product = product * c
            sum = sum + c 
        
        return product - sum