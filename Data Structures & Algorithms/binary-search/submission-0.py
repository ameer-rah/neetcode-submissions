class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mean = (left + right) // 2
            if nums[mean] == target:
                return mean
            elif nums[mean] < target:
                left = mean + 1
            else:
                right = mean - 1
        return -1