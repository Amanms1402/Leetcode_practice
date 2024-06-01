class Solution:
    def minOperations(self, nums: List[int]) -> int:
        return -1 if 1 in (v:=Counter(nums).values()) else sum(ceil(f/3) for f in v)