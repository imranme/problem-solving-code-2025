class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a", "e", "i", "o", "u"}

        is_vowel_string = [
            1 if word[0] in vowels and word[-1] in vowels else 0
            for word in words
        ]   

        n = len(words)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + is_vowel_string[i]
        res = []
        for start, end in queries:
            res.append(prefix_sum[end + 1] - prefix_sum[start])
        return res