class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(a, b):
            gg = len(a)
            if gg > len(b):
                return False
            return a == b[:gg] and a == b[-gg:]
        
        l = len(words)
        ans = 0
        for x in range(l-1):
            for y in range(x + 1, l):
                if isPrefixAndSuffix(words[x], words[y]):
                    ans += 1
        return ans