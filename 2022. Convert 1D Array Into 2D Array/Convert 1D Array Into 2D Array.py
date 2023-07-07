class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        twod=[]
        start=0
        if m*n==len(original):
            temp=n
            for i in range(m):
                twod.append(original[start:n])
                start=n
                n+=temp
            return twod
        else:
            return []