class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_max, curr_alt = 0, 0
        for i in range(len(gain)):
            curr_alt = curr_alt + gain[i]
            if curr_alt > curr_max:
                curr_max = curr_alt
        return curr_max