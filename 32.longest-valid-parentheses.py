#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (23.44%)
# Total Accepted:    132.8K
# Total Submissions: 566.7K
# Testcase Example:  '"(()"'
#
# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
# 
# Example 1:
# 
# 
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# 
# 
# Example 2:
# 
# 
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"
# 
# 
#
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
