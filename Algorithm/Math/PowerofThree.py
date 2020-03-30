import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 3: return False
        res = math.log10(n) / math.log10(3)
        return res == int(res)