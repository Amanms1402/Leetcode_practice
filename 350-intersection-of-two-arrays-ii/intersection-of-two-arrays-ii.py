class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        counting1: list[int] = [0 for _ in range(1001)]
        counting2: list[int] = [0 for _ in range(1001)]

        for n in nums1:
            counting1[n] += 1

        for n in nums2:
            counting2[n] += 1

        res: list[int] = []
        for number in range(1001):
            c1: int = counting1[number]
            c2: int = counting2[number]
            mn: int = min(c1, c2)
            for _ in range(mn):
                res.append(number)

        return res