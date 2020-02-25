# -*- coding: UTF-8 -*-

'''
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of
your product fails the quality check. Since each version is developed based on the previous version, all the versions
after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following
ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find
the first bad version. You should minimize the number of calls to the API.
'''

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n
        while left <= right:
            mid = left + (right - left) // 2
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid - 1
            if isBadVersion(mid) + isBadVersion(mid+1) == 1:
                if isBadVersion(mid) == 1:
                    return mid
                else:
                    return mid+1
            if isBadVersion(mid) + isBadVersion(mid-1) == 1:
                if isBadVersion(mid) == 1:
                    return mid
                else:
                    return mid-1

# TODO：Following method do not need any specific condition.
'''
public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int lo = 0;
        int hi = n;

        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;

            if (isBadVersion(mid)) {
                hi = mid - 1;
            } else {
                lo = mid + 1;
            } 
        }
        return lo;
    }
}

作者：thirtyyuan
链接：https://leetcode-cn.com/problems/first-bad-version/solution/shi-yong-er-fen-fa-de-biao-zhun-mo-ban-yi-lai-jie-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''