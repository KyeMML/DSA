'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
'''

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # beign new accumulating sum list with 0
        self.accu = [0]
        #calculate to running total by adding nums to most recent total in accu
        for num in nums:
            self.accu.append(self.accu[-1] + num)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        # return the sum at accu j+1 ( the plus one is to compensate for the first index now as 0), minus the sum at i to give the sum between i and j inclusive. 
        return self.accu[j+1] - self.accu[i]
