class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2: return True
        l, r = 1, num//2
        while l <= r:
            m = l + (r - l) // 2
            if m ** 2 < num:
                l = m + 1
            elif m ** 2 > num:
                r = m - 1
            elif m ** 2 == num:
                return True
        return False

class Solution2:
    def isPerfectSquare(self, num: int) -> bool:
        x = num // 2
        while x ** 2 - num >= 0:
            if x ** 2 - num == 0:
                return True
            x = (x + num / x) // 2
        return False

if __name__ == '__main__':
    print(Solution2().isPerfectSquare(num=16))