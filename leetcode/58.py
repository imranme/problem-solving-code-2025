# https://leetcode.com/problems/length-of-last-word/description/ 

# s = input().strip()     # ইনপুট নাও (শুরু/শেষের স্পেস কেটে দেবে)
# words = s.split()       # স্পেস দিয়ে ভাঙো
# print(len(words[-1])) 

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()       # space দিয়ে split
        return len(words[-1])   # last word length



class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split(' ')[-1])


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1
        
        # skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1
        
        # count last word length
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
            
        return length

