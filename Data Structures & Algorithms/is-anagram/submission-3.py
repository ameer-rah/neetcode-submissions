class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap_S = {}
        for char in s:
            hashmap_S[char] = hashmap_S.get(char, 0) + 1
        
        hashmap_T = {}
        for char in t:
            hashmap_T[char] = hashmap_T.get(char, 0) + 1
        
        if hashmap_S == hashmap_T:
            return True
        else:
            return False
        
"""
notes:
- create a hashmap for string s
- store each char in string s hashmap
- create a hashmap for string t
- store each char in string t hashmap
- if hashmapS == hashmapT, then return true
- otherwise return false
"""