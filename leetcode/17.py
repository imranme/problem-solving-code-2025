class Solution:
    def maxScore(self, s: str) -> int:
        total_one = s.count('1')

        max_score = 0
        left_zero = 0
        right_one = total_one

        for i in range(len(s) - 1):
            if s[i] == '0':
                left_zero += 1
            else:
                right_one -= 1
            max_score = max(max_score, left_zero + right_one)
        return max_score

        