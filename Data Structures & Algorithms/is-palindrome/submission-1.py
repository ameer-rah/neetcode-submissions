class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ""
        for char in s:
            if char.isalnum():
                newString += char.lower()

        left = 0
        right = len(newString) - 1

        while left < right:
            if newString[left] != newString[right]:
                return False
            left += 1
            right -= 1
        return True


"""
notes:
- make the string alphanumeric

dsa: two pointers
- create a new string 
- loop through the old string 
    - if char is alphanumeric
        - add to new string with lowercase char
- create left and right pointer
- if the char in the left pointer != char in right pointer
    - return false
"""