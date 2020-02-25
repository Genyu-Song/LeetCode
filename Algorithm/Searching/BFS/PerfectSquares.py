# -*- coding: UTF-8 *-

'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
'''

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # TODO: use list.pop() instead of list[0]; del list[0]
        square_number = [i for i in range(1, int(n**.5) + 1)]
        know_result = {}
        know_result[n] = 0
        search_list = [n]
        while True:
            for residuals in search_list:
                for sn in square_number:
                    if residuals - sn * sn >= 0:
                        if not know_result.__contains__(residuals - sn * sn):
                            know_result[residuals - sn * sn] = know_result[residuals] + 1
                            if residuals - sn * sn == 0:
                                return know_result[0]
                            else:
                                search_list.append(residuals - sn * sn)
            try:
                return know_result[0]
            except:
                return -1


# class node:
#     def __init__(self, value, step=0):
#         self.value = value
#         self.step = step
#
#     def __str__(self):
#         return '<value:{}, step:{}>'.format(self.value, self.step)
#
#
# class Solution:
#     def numSquares(self, n: int) -> int:
#         queue = [node(n)]
#         visited = set([node(n).value])
#
#         while queue:
#             vertex = queue.pop(0)
#             residuals = [vertex.value - n * n for n in range(1, int(vertex.value ** .5) + 1)]
#             for i in residuals:
#                 new_vertex = node(i, vertex.step + 1)
#                 if i == 0:
#                     return new_vertex.step
#
#                 elif i not in visited:
#                     queue.append(new_vertex)
#                     visited.add(i)
#         return -1

if __name__ == '__main__':
    print(Solution().numSquares(n=19))