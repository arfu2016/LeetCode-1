# Time:  addNum: O(n), getIntervals: O(n), n is the number of disjoint intervals.
# Space: O(n)

# Given a data stream input of non-negative integers a1, a2, ..., an, ...,
# summarize the numbers seen so far as a list of disjoint intervals.
#
# For example, suppose the integers from the data stream are 1, 3, 7, 2, 6,
# ..., then the summary will be:
#
# [1, 1]
# [1, 1], [3, 3]
# [1, 1], [3, 3], [7, 7]
# [1, 3], [7, 7]
# [1, 3], [6, 7]
#
# Follow up:
# What if there are lots of merges and the number of disjoint intervals
# are small compared to the data stream's size?

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__intervals = []

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        def upper_bound(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) / 2
                if nums[mid].start > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        if not self.__intervals:
            self.__intervals.append(Interval(val, val))
        else:
            i = upper_bound(self.__intervals, val)
            if i == len(self.__intervals):
                if self.__intervals[i - 1].end + 1 == val:
                    self.__intervals[i - 1].end = val
                elif self.__intervals[i - 1].end + 1 < val:
                    self.__intervals.insert(i, Interval(val, val))
            else:
                if i != 0 and self.__intervals[i - 1].end + 1 == val:
                    self.__intervals[i - 1].end = val
                elif i == 0 or self.__intervals[i - 1].end + 1 < val:
                    self.__intervals.insert(i, Interval(val, val))
                i = upper_bound(self.__intervals, val)
                if self.__intervals[i - 1].end + 1 == self.__intervals[i].start:
                    self.__intervals[i - 1].end = self.__intervals[i].end
                    del self.__intervals[i]

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.__intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()