# 5337

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        chara = ['a', 'e', 'i', 'o', 'u']
        N = len(s)
        dp = [0 for _ in range(N)]

        def is_valid(times, flag=True):
            for ind, val in times.items():
                if val % 2 != 0:
                    flag = False
            return flag

        for i in range(N):
            times = {}

            if s[i] in chara:
                times[s[i]] = times.get(s[i], 0) + 1
                tempo = 0
                count = 0
            else:
                tempo = 1
                count = 1

            for j in range(i+1, N):
                if s[j] in chara:
                    times[s[j]] = times.get(s[j], 0) + 1
                    if is_valid(times):
                        tempo = j - i + 1
                        count = tempo
                else:
                    if is_valid(times):
                        count += 1
            dp[i] = max(tempo, count)
        return max(dp)

class Solution2: # TODO: Review
    def findTheLongestSubstring(self, s: str) -> int:
        cur = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        memory = {(0, 0, 0, 0, 0): 0}
        res = 0
        for index, chara in enumerate(s):
            if chara in cur:
                cur[chara] ^= 1
            key = tuple(val for index, val in cur.items())
            if key in memory:
                res = max(res, index - memory[key] + 1)
            else:
                memory[key] = index + 1
        return res

if __name__ == '__main__':
    print(Solution2().findTheLongestSubstring(s="id"))