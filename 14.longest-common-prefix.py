#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (31.75%)
# Total Accepted:    293.5K
# Total Submissions: 924.6K
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# Example 1:
# 
# 
# Input: ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# Note:
# 
# All given inputs are in lowercase letters a-z.
# 
#
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
