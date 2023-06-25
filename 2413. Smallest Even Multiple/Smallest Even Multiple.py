class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n<=0:
            return 0
        elif n==1:
            return 2
        else:

            for i in range(n,n**2):
                if i%2==0 and i%n==0:
                    return i
        