class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: list[int], verticalCuts: list[int]) -> int:

        horizontalCuts.sort()
        verticalCuts.sort()

        max_height = 0
        prev = 0

        for cut in horizontalCuts:
            max_height = max(max_height, cut - prev)
            prev = cut

        max_height = max(max_height, h - prev)

        max_width = 0
        prev = 0

        for cut in verticalCuts:
            max_width = max(max_width, cut - prev)
            prev = cut

        max_width = max(max_width, w - prev)

        return (max_height * max_width) 
