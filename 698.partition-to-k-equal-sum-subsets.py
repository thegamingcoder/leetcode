#
# [698] Partition to K Equal Sum Subsets
#
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/
#
# algorithms
# Medium (38.13%)
# Total Accepted:    17.4K
# Total Submissions: 45.6K
# Testcase Example:  '[4,3,2,3,5,2,1]\n4'
#
# Given an array of integers nums and a positive integer k, find whether it's
# possible to divide this array into k non-empty subsets whose sums are all
# equal.
# 
# Example 1:
# 
# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3),
# (2,3) with equal sums.
# 
# 
# 
# Note:
# 1 .
# 0 < nums[i] < 10000.
# 
#
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
