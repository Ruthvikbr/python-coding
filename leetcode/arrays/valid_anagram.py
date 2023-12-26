from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s = list(s)
        t = list(t)
        s = Counter(s)
        t = Counter(t)
        return s == t

# Accepts two strings. If the length of two strings are different, it cannot be an Anagram.
# Compare the Counter dictionaries of both