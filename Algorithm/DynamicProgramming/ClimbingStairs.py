# -*- coding: UTF-8 -*-

'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [1, 2]
        count = 0

        def dfs(target=n, path=[]):
            if target == 0:
                nonlocal count
                count += 1
                return

            for step in steps:
                residue = target - step
                if residue < 0:
                    return
                else:
                    path.append(step)
                    dfs(residue, path)
                    path.pop()

        dfs()
        return count

class Solution2:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]

if __name__ == '__main__':
    print(Solution2().climbStairs(n=3))