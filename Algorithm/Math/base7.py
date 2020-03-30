class Solution:
    def convertToBase7(self, num: int) -> str:
        flag = True if num < 0 else False
        num = abs(num)
        res = []
        while True:
            if num < 7:
                res.insert(0, str(num))
                break
            mod = str(num % 7)
            res.insert(0, mod)
            num //= 7
        if flag: res.insert(0, '-')
        return ''.join(res)

if __name__ == '__main__':
    print(Solution().convertToBase7(num=-7))