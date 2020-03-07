# -*- coding: UTF-8 -*-

'''
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature.
For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we
defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith
and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend
circles among all the students.
'''

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if len(M) == 0: return 0
        R, C = len(M), len(M[0])

        def dfs(i, j):
            if 0 <= i < C and 0 <= j < R and M[j][i] == 1:
                M[j][i] = 0
                for m in range(R):
                    if M[m][i] == 1:
                        dfs(i, m)

                for n in range(C):
                    if M[j][n] == 1:
                        dfs(n, j)

        count = 0
        for r in range(R):
            for c in range(C):
                if M[r][c]:
                    dfs(c, r)
                    count += 1
        return count

class Solution2: # Union-Find
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        class UnionFind:
            def __init__(self, n):
                self.count = n
                self.parent = [i for i in range(n)]
                self.size = [1 for i in range(n)]

            def get_count(self):
                return self.count

            def union(self, p, q):
                p_root = self.find(p) # TODO：注意这边应该用的是root！不然合并root会出错！
                q_root = self.find(q)
                if self.find(p_root) == self.find(q_root):
                    return

                if self.size[p_root] >= self.size[q_root]:
                    self.parent[q_root] = self.parent[p_root]
                    self.size[q_root] += self.size[p_root]
                else:
                    self.parent[p_root] = self.parent[q_root]
                    self.size[p_root] += self.size[q_root]

                self.count -= 1

            def find(self, p):
                while self.parent[p] != p:
                    # 路径压缩
                    self.parent[p] = self.parent[self.parent[p]]
                    p = self.parent[p]
                return p

            def is_connected(self, p, q):
                return self.find[p] == self.find[q]

        n = len(M)
        UF = UnionFind(n)
        for i in range(n):
            for j in range(i):
                if M[i][j] == 1:
                    UF.union(j, i)
        return UF.get_count()

class Solution3: # BFS
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        queue = []
        visited = set()
        count = 0

        def bfs(i):
            queue.append(i)
            while queue:
                i = queue.pop(0)
                for j in range(len(M[i])):
                    if j not in visited and M[i][j]:
                        queue.append(j)
                        visited.add(j)

        for i in range(len(M)):
            if i not in visited:
                bfs(i)
                count += 1
        return count

class Solution4: # DFS
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        count = 0
        N = len(M)
        known_result = set()

        def dfs(n):
            for x in range(N):
                if x not in known_result and M[n][x]:
                    known_result.add(x)
                    dfs(x)

        for i in range(N):
            if i not in known_result:
                dfs(i)
                count += 1

        return count


if __name__ == '__main__':
    print(Solution4().findCircleNum(M=[[1,0,0,1],
                                       [0,1,0,1],
                                       [0,0,1,0],
                                       [1,1,0,1]]))