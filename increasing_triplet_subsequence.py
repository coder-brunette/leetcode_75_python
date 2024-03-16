# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and 
# nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

# class Solution:
#     def increasingTriplet(self, nums: List[int]) -> bool:
#         i = 0
#         while i < len(nums):
#             current_char = nums[i]

#         while i < len(nums) and nums[i] == current_char:
#             if current_char < nums[i+1]:
#                 if nums[i+1] < nums[i+2]:
#                     return True
#             i += 1
#             else:
#                 return False

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_min = float('inf')  
        second_min = float('inf')
        
        for num in nums:
            if num <= first_min:
                first_min = num  
            elif num <= second_min:
                second_min = num 
            else:
                return True 

        return False  
