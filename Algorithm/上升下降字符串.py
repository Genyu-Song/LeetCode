class Solution:
    def sortString(self, s: str) -> str:
        # test = {'a': 1, 'b': 2}
        # for ind, val in test.items():
        #     print(val)
        if not s: return ''

        s = list(s)
        res = []
        while s:
            c_list = list(set(s))
            c_list.sort(key=lambda c: ord(c))
            for i in c_list:
                res.append(i)
                s.remove(i)

            c_list = list(set(s))
            c_list.sort(key=lambda c: ord(c), reverse=True)
            for i in c_list:
                res.append(i)
                s.remove(i)
        return ''.join(res)

if __name__ == '__main__':
    print(Solution().sortString(s='aabbcc'))