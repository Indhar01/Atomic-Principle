class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element=0
        digit=0
        for i in nums:
            element+=i
            if i>9:
                temp=0
                while i>0:
                    temp=i%10
                    digit+=temp
                    i=i//10

            else:
                digit+=i

        return element-digit