#
# [778] Reorganize String
#
# https://leetcode.com/problems/reorganize-string/description/
#
# algorithms
# Medium (36.79%)
# Total Accepted:    7.5K
# Total Submissions: 20.4K
# Testcase Example:  '"aab"'
#
# Given a string S, check if the letters can be rearranged so that two
# characters that are adjacent to each other are not the same.
# 
# If possible, output any possible result.  If not possible, return the empty
# string.
# 
# Example 1:
# 
# 
# Input: S = "aab"
# Output: "aba"
# 
# 
# Example 2:
# 
# 
# Input: S = "aaab"
# Output: ""
# 
# 
# Note:
# 
# 
# S will consist of lowercase letters and have length in range [1, 500].
# 
# 
# 
#
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
