# -*- coding: UTF-8 -*-

class Solution2(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = defaultdict(list)
        for r, c in reservedSeats:
            rows[r].append(c)

        ans, groups = 2 * (n-len(rows)), [[2, 5], [4, 7], [6, 9]]
        for taken in rows.values():
            ok = [all(not (l <= c <= r) for c in taken) for (l, r) in groups]
            ans += 2 if ok[0] and ok[2] else any(ok)
        return ans

from typing import List
from collections import defaultdict
class Solution3:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        res = 0
        dic = defaultdict(list)
        for r, c in reservedSeats:
            dic[r].append(c)

        for i in dic:
            cnt = all([j not in dic[i] for j in range(2, 6)]) + all([j not in dic[i] for j in range(6, 10)])
            if cnt == 0:
                cnt += all([j not in dic[i] for j in range(4, 8)])
            res += cnt
        return res + 2 * (n - len(dic.keys()))

if __name__ == '__main__':
    print(Solution2().maxNumberOfFamilies(n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]))