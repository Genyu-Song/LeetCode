from typing import List

class Solution: # 暴力法
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        for i in range(len(nums)-1):
            for j in range(1, len(nums)):
                zeros = nums[i:j+1].count(0)
                ones = nums[i:j+1].count(1)
                if zeros == ones:
                    max_len = max(max_len, j-i+1)
        return max_len

class Solution2: # 找出现相同的count
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {}
        dic[0] = -1
        max_len = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            elif nums[i] == 1:
                count -= 1
            if count not in dic:
                dic[count] = i
            else:
                max_len = max(max_len, i - dic[count])
        return max_len

if __name__ == '__main__':
    print(Solution2().findMaxLength(nums=[0,1,0]))