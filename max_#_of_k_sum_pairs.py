# You are given an integer array nums and an integer k.

# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
# Return the maximum number of operations you can perform on the array.

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        sum = 0
        count = 0
        left_pointer = 0
        right_pointer = len(nums) - 1

        nums.sort()
        while left_pointer < right_pointer:
            sum = nums[left_pointer] + nums[right_pointer]
            if sum == k:
                count += 1
                left_pointer += 1
                right_pointer -= 1
            elif sum < k:
                left_pointer += 1
            else:
                right_pointer -= 1
        return count