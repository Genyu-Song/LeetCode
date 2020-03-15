from collections import Counter
from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        for i in range(len(nums)-1):
            for j in range(1, len(nums)):
                zeros = Counter(nums[i, j+1], 0)
                ones = Counter(nums[i, j+1], 1)
                if zeros == ones:
                    max_len = max(max_len, j-i+1)
        return max_len

if __name__ == '__main__':
    print(Solution().findMaxLength(nums=[0,1,0]))