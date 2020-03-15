# -*- coding: UTF-8 -*-

'''
给定一个32位正整数 n，你需要找到最小的32位整数，其与 n 中存在的位数完全相同，并且其值大于n。如果不存在这样的32位整数，则返回-1。
'''

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n, tails = list(str(n)), []
        for i in range(len(n)-1, -1, -1):
            for j in tails:
                if n[j] > n[i]:
                    n[j], n[i] = n[i], n[j]
                    m = int(''.join(n[:i+1] + sorted(n[i+1:])))
                    return m if m < 2**31 - 1 else -1
            tails.append(i)
        return -1

if __name__ == '__main__':
    print(Solution().nextGreaterElement(n=21))