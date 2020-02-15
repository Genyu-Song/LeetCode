# -*- coding: UTF-8 -*-

'''
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie. Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content with; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

Note:
You may assume the greed factor is always positive.
You cannot assign more than one cookie to one child.
'''

# TODO: a = sorted(a, key=, reverse=) OR a.sort(key=, reverse=)

class Solution:
    def findContentChildren(self, g, s):
        children = [[i, 0] for i in g]
        children.sort(key=lambda x: x[0], reverse=True)
        s = sorted(s, reverse=True)
        count = 0
        child = 0
        for cookies in s:
            flag = False
            while child < len(g) and flag == False:
                if cookies >= children[child][0]:
                    count += 1
                    flag = True
                child += 1
        return count


class Solution2(object):
    # 更清晰一点
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        res = 0
        g.sort()
        s.sort()

        g_length = len(g)
        s_length = len(s)

        i = 0
        j = 0
        while i < g_length and j < s_length:
            if g[i] <= s[j]:
                # 可以满足胃口，把小饼干喂给小朋友
                res += 1
                i += 1
                j += 1
            else:
                # 不满足胃口，查看下一块小饼干
                j += 1

        return res


if __name__ == '__main__':
    print(Solution().findContentChildren(g=[10,9,8,7], s=[5,6,7,8]))