class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product=1
        sumval=0

        while n>0:
            temp=n%10
            product*=temp
            sumval+=temp
            n=n//10

        return product-sumval