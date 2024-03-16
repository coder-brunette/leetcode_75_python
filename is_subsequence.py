# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the 
# characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" 
# while "aec" is not).

class Solution:
    # def isSubsequence(self, s: str, t: str) -> bool:
    #     slst = list(s)
    #     tlst = list(t)
    #     dct = {}
    #     bool_val = False
    #     i = 0
    #     while i in range(len(slst)):
    #         if slst[i] in tlst:
    #             dct[slst[i]] = tlst.index(slst[i])
    #         else:
    #             return bool_val
    #         i += 1
    #     bool_val = list(dct.values()) == sorted(dct.values())
    #     return bool_val
    
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)
