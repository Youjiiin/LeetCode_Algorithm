class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        start = 0
        end = len(height) - 1

        while start < end:
            w = end - start
            max_water = max(max_water, w * min(height[start], height[end]))

            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        
        return max_water