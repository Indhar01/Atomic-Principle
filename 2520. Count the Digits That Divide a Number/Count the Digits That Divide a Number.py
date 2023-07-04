class Solution:
    def countDigits(self, num: int) -> int:
        count=0
        div=[int(x) for x in str(num)]
        for i in div:
            if num % i==0:
                count+=1
        return count
        