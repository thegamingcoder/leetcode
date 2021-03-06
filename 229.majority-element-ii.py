#
# [229] Majority Element II
#
# https://leetcode.com/problems/majority-element-ii/description/
#
# algorithms
# Medium (29.62%)
# Total Accepted:    74.8K
# Total Submissions: 252.5K
# Testcase Example:  '[3,2,3]'
#
# Given an integer array of size n, find all elements that appear more than ⌊
# n/3 ⌋ times.
# 
# Note: The algorithm should run in linear time and in O(1) space.
# 
# Example 1:
# 
# 
# Input: [3,2,3]
# Output: [3]
# 
# Example 2:
# 
# 
# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]
# 
#
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
