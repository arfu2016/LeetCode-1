# Time:  O(n)
# Space: O(1), no extra space
#
# Given an array of integers, every element appears twice except for one. Find that single one.
# 
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#

import operator


class Solution:
    """
    :type nums: List[int]
    :rtype: int
    """
    def singleNumber(self, A):
        return reduce(operator.xor, A)
    # reduce is all to one, operator.xor can select the unique one from several couples

if __name__ == '__main__':
    print Solution().singleNumber([1, 1, 2, 2, 3])
    # the test result should be 3
