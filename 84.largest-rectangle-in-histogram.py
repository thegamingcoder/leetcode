#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (28.08%)
# Total Accepted:    124.5K
# Total Submissions: 443.6K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# Given n non-negative integers representing the histogram's bar height where
# the width of each bar is 1, find the area of largest rectangle in the
# histogram.
# 
# 
# Above is a histogram where width of each bar is 1, given height =
# [2,1,5,6,2,3].
# 
# 
# 
# 
# The largest rectangle is shown in the shaded area, which has area = 10
# unit.
# 
# 
# 
# Example:
# 
# 
# Input: [2,1,5,6,2,3]
# Output: 10
# 
# 
#
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
