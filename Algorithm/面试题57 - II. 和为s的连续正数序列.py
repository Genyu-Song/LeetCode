from typing import List
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        output = []

        for i in range(1, target // 2 + 1):
            last_sum = 0
            flag = False
            j = i
            path = []
            while flag == False and last_sum <= target:
                if last_sum == target:
                    output.append(path[:])
                    path = []
                    flag = True
                elif last_sum < target:
                    last_sum = last_sum + j
                    path.append(j)
                elif tmp_sum > target:
                    path = []
                j += 1

        return output

if __name__ == '__main__':
    print(Solution().findContinuousSequence(target=15))