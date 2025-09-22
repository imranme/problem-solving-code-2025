class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)                     # count frequencies
        max_freq = max(freq.values())            # find maximum frequency
        total = sum(v for v in freq.values() if v == max_freq)  # sum them
        return total
        