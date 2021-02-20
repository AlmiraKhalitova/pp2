class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        diction = dict()
        pairs = 0
        for num in nums:
            if num in diction:
                pairs += diction[num]
                diction[num] += 1
            else:
                diction[num] = 1
        return pairs