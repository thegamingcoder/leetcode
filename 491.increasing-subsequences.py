#
# [491] Increasing Subsequences
#
# https://leetcode.com/problems/increasing-subsequences/description/
#
# algorithms
# Medium (39.03%)
# Total Accepted:    19.8K
# Total Submissions: 50.8K
# Testcase Example:  '[4,6,7,7]'
#
# 
# Given an integer array, your task is to find all the different possible
# increasing subsequences of the given array, and the length of an increasing
# subsequence should be at least 2 .
# 
# 
# Example:
# 
# Input: [4, 6, 7, 7]
# Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7],
# [4,7,7]]
# 
# 
# 
# Note:
# 
# The length of the given array will not exceed 15.
# The range of integer in the given array is [-100,100].
# The given array may contain duplicates, and two equal integers should also be
# considered as a special case of increasing sequence.
# 
# 
#
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
