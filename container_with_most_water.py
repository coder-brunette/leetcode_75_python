# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith 
# line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        left_pointer = 0
        right_pointer = len(height) - 1

        while left_pointer < right_pointer:
            width = right_pointer - left_pointer
            ht = min(height[right_pointer], height[left_pointer])
            curr_water = width * ht
            if max_water < curr_water:
                max_water = curr_water
            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
        return max_water