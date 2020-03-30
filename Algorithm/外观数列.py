class Solution:
    def countAndSay(self, n: int) -> str:
        def dfs(target, level=1):
            if level == n: return target
            level += 1
            temp_res = []
            count = 1
            i = 0
            while True:
                if i == len(target) - 1:
                    if target[i] == target[-1]:
                        temp_res += [count] + [target[i]]
                    else:
                        temp_res += [count] + [target[-1]] + [target[i]]
                    break
                if target[i + 1] == target[i]:
                    count += 1
                else:
                    temp_res += [count] + [target[i]]
                    count = 1
                i += 1

            return dfs(temp_res, level)

        res = dfs([1], 1)
        return ''.join(str(e) for e in res)

if __name__ == '__main__':
    print(Solution().countAndSay(n=4))