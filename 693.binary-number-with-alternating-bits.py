#
# [693] Binary Number with Alternating Bits
#
# https://leetcode.com/problems/binary-number-with-alternating-bits/description/
#
# algorithms
# Easy (56.18%)
# Total Accepted:    24.7K
# Total Submissions: 44K
# Testcase Example:  '5'
#
# Given a positive integer, check whether it has alternating bits: namely, if
# two adjacent bits will always have different values.
# 
# Example 1:
# 
# Input: 5
# Output: True
# Explanation:
# The binary representation of 5 is: 101
# 
# 
# 
# Example 2:
# 
# Input: 7
# Output: False
# Explanation:
# The binary representation of 7 is: 111.
# 
# 
# 
# Example 3:
# 
# Input: 11
# Output: False
# Explanation:
# The binary representation of 11 is: 1011.
# 
# 
# 
# Example 4:
# 
# Input: 10
# Output: True
# Explanation:
# The binary representation of 10 is: 1010.
# 
# 
#
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
