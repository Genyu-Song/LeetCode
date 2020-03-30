class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        L, R = [0 for _ in range(N)], [0 for _ in range(N)]
        for i in range(N):
            if i == 0:
                L[0] = 1
                R[N-1] = 1
            else:
                L[i] = nums[i-1] * L[i-1]
                R[N-1-i] = nums[N-i] * R[N-i]
        return map(lambda a, b: a*b, L, R)

class Solution2: # 压缩空间复杂度
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        L = [0 for _ in range(N)]
        R = 1
        for i in range(N):
            if i == 0:
                L[0] = 1
            else:
                L[i] = nums[i-1] * L[i-1]
        for i in range(N-1, -1, -1):
            L[i] = L[i] * R
            R *= nums[i]
        return L