'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

source - https://leetcode.com/problems/climbing-stairs/

'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        store = {}
        def helper(n):
            # Base Cases
            if n == 1 or n == 2:
                return n
            # checking if we have done it before in memoization
            elif n in store:
                return store[n]
            # if not a base case and not done before, then we use recursion to reach the base cases
            else:
                # Recursion in fibonnaci sequence, as every stairs length N > 2 is the accumulation of choices between 1 or 2 steps. 
                store[n] = helper(n-1) + helper(n-2)
                return store[n]
        return helper(n)
