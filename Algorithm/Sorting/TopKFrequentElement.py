# -*- coding: UTF-8 -*-

'''
Given a non-empty array of integers, return the k most frequent elements.
'''

# 1. Quick Select
# 2. Minimum Heap
# 3. collections.Counter()

class heapify(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        def swap(nums, index1, index2):
            nums[index1], nums[index2] = nums[index2], nums[index1]

        def flowup(nums, data):
            nums.append(data)
            index = len(nums) - 1
            parent_index = index >> 1
            while parent_index is not None and parent_index != 0:
                if nums[index][1] < nums[parent_index][1]:
                    swap(nums, index, parent_index)
                    index = parent_index
                    parent_index = index >> 1
                else:
                    break
            return

        def bubbledown(nums, data):
            nums.append(data)
            if nums[1][1] > nums[len(nums)-1][1]:
                del nums[len(nums) - 1]
                return
            else:
                swap(nums, 1, len(nums) - 1)
                del nums[len(nums) - 1]
            last_index = len(nums) - 1
            index = 1
            while True:
                smallest_index = index
                if 2 * index <= last_index and nums[2 * index][1] < nums[smallest_index][1]:
                    smallest_index = 2 * index
                if 2 * index + 1 <= last_index and nums[2 * index + 1][1] < nums[smallest_index][1]:
                    smallest_index = 2 * index + 1
                if smallest_index == index:
                    break
                swap(nums, index, smallest_index)
                index = smallest_index
            return

        map_dict = {}
        for i in nums:
            if i in map_dict.keys():
                map_dict[i] += 1
            else:
                map_dict[i] = 1

        map_arr = list(map_dict.items())
        heap = [(0, 0)]
        for i in map_arr:
            if len(heap) < k + 1:
                flowup(heap, i)
            else:
                bubbledown(heap, i)
        return [i[0] for i in heap[-1:0:-1]]

class Solution:
    def topKFrequent(self, nums, k):
        def heapify(arr, n, i):
            smallest = i  # 构造根节点与左右子节点
            l = 2 * i + 1
            r = 2 * i + 2
            if l < n and arr[l][1] < arr[i][1]:  # 如果左子节点在范围内且小于父节点
                smallest = l
            if r < n and arr[r][1] < arr[smallest][1]:
                smallest = r
            if smallest != i:  # 递归基:如果没有交换，退出递归
                arr[i], arr[smallest] = arr[smallest], arr[i]
                heapify(arr, n, smallest)  # 确保交换后，小于其左右子节点

        # 哈希字典统计出现频率
        map_dict = {}
        for item in nums:
            if item not in map_dict.keys():
                map_dict[item] = 1
            else:
                map_dict[item] += 1

        map_arr = list(map_dict.items())
        lenth = len(map_dict.keys())
        # 构造规模为k的minheap
        if k <= lenth:
            k_minheap = map_arr[:k]
            # 从后往前建堆，避免局部符合而影响递归跳转，例:2,1,3,4,5,0
            for i in range(k // 2 - 1, -1, -1):
                heapify(k_minheap, k, i)
            # 对于k:, 大于堆顶则入堆，维护规模为k的minheap
            for i in range(k, lenth): # 堆建好了，没有乱序，从前往后即可
                if map_arr[i][1] > k_minheap[0][1]:
                    k_minheap[0] = map_arr[i] # 入堆顶
                    heapify(k_minheap, k, 0)  # 维护 minheap
        # 如需按顺序输出，对规模为k的堆进行排序
        # 从尾部起，依次与顶点交换再构造minheap，最小值被置于尾部
        for i in range(k - 1, 0, -1):
            k_minheap[i], k_minheap[0] = k_minheap[0], k_minheap[i]
            k -= 1 # 交换后，维护的堆规模-1
            heapify(k_minheap, k, 0)
        return [item[0] for item in k_minheap]

class BucketSort:
    def topKFrequent(self, nums, k):
        map_dict = {}
        for i in nums:
            map_dict[i] = map_dict.get(i, 0) + 1
        max_time = max(map_dict.values())
        bucket_list = [[] for i in range(max_time+1)]
        for key, value in map_dict.items():
            bucket_list[value].append(key)
        res = []
        for i in range(max_time, -1, -1):
            if bucket_list[i]:
                res.extend(bucket_list[i])
            if len(res) >= k:
                return res[:k]


if __name__ == '__main__':
    print(BucketSort().topKFrequent(nums=[1,1,1,1,1,2,2,2,3,3,4,4,5,6], k=4))
    for i in range(6 // 2 - 1, -1, -1):
        print(i)