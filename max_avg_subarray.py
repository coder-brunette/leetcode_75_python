# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
# Any answer with a calculation error less than 10-5 will be accepted.

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        w_sum = sum(nums[:k])
        avg = w_sum/k

        for i in range(k,len(nums)):
            w_sum = w_sum + nums[i] - nums[i-k]
            new_avg = w_sum/k
            avg = max(avg, new_avg)

        return avg
        