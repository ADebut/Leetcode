class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        maxA = min(height[i], height[j]) * (j - i)
        while(i < j):
            if height[i] < height[j]:
                i += 1
                maxA = max(min(height[i], height[j]) * (j - i), maxA)
            elif height[i] == height[j]:
                i += 1
                j -= 1
                maxA = max(min(height[i], height[j]) * (j - i), maxA)
            elif height[i] > height[j]:
                j -= 1
                maxA = max(min(height[i], height[j]) * (j - i), maxA)
        return maxA