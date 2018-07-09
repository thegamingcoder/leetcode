#
# [132] Palindrome Partitioning II
#
# https://leetcode.com/problems/palindrome-partitioning-ii/description/
#
# algorithms
# Hard (25.23%)
# Total Accepted:    84.5K
# Total Submissions: 335.1K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
# 
# Return the minimum cuts needed for a palindrome partitioning of s.
# 
# Example:
# 
# 
# Input: "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1
# cut.
# 
# 
#
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        
