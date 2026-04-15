class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        charDict = {
            ")" : "(",
            "]" : "[",
            "}" : "{",
        }

        for char in s:
            if char in charDict:
                if stack and stack[-1] == charDict[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack

        
"""
notes:
- dsa: stack
- create a stack
- create a dictionary of all the characters
- loop through the input string
    -  if char is in dictionary:
        - if the char in the front and back are in the dictionary
            - stack.pop
        - else:
            - return False
    - else:
        - append char until you find the closing bracket
"""