class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        S = {}
        for i in nums:
            S[i] = S.get(i, 0) + 1
            if S[i]>1: return True
        return False