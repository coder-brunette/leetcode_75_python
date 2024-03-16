# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        str3 = ''
        for i,j in zip(word1,word2):
            str3 += i+j
        min_len = min(len(word1), len(word2))
        if len(word1) > len(word2):
            str3 += word1[min_len:]
        else:
            str3 += word2[min_len:]
        return str3