class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = set()

        for num in nums:
            if num in hashmap:
                return True
            else:
                hashmap.add(num)
        return False

"""
notes:
- store the amount of times a number is inside an array
- if it is more than once, return true
- if not, return false

create a hashmap with a set (sets have no repeated numbers):
- once we see an elem we store it in hashmap
- if the elem is seen more than once, return true
- else return false
- return false

Time: O(n)
Space: O(n)
"""
        