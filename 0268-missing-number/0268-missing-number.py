class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(max(nums) + 1):
            if i != nums[i]:
                return i
        return max(nums) + 1
        