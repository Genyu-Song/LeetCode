# -*- coding: UTF-8 -*-

'''
Given a string, sort it in decreasing order based on the frequency of characters.
'''

# 1. Bucket Sort
# 2. Quick Selection

class Solution:
    def frequencySort(self, s):
        # Bucket Sort
        map_dict = {}
        for i in list(s):
            map_dict[i] = map_dict.get(i, 0) + 1

        try:
            max_times = max(map_dict.values())
            bucket_list = [[] for i in range(max_times + 1)]
            for key, value in map_dict.items():
                bucket_list[value].append(key)
            res = []
            for i in range(max_times, -1, -1):
                for c in bucket_list[i]:
                    count = 0
                    while count < i:
                        res += c
                        count += 1
        except: return ''
        return ''.join(res)

import collections

class Solution2:
    def frequencySort(self, s):
        return ''.join([i * j for i, j in collections.Counter(s).most_common()])

class Solution3:
    '''
    TODO: Review
    '''
    def heap_sort(self, s, k=-1):
        def flowup(nums, index):
            parent_index = index >> 1
            if parent_index is not None and parent_index != 0:
                if nums[parent_index][1] < nums[index][1]:
                    swap(nums, parent_index, index)
                    index = parent_index
                    flowup(nums, index)

        def bubbledown(nums, index):
            left, right = index * 2, index * 2 + 1
            maximum = index
            length = len(nums)
            if left <= length - 1 and nums[left][1] > nums[maximum][1]:
                maximum = left
            if right <= length - 1 and nums[right][1] > nums[maximum][1]:
                maximum = right
            if maximum != index:
                swap(nums, index, maximum)
                bubbledown(nums, maximum)

        def swap(nums, index1, index2):
            nums[index1], nums[index2] = nums[index2], nums[index1]

        def build(s, k):
            if k == -1: k=len(s)
            heap = [0]
            for i in range(len(s)):
                heap.append(s[i])
                if len(heap) <= k + 1:
                    flowup(heap, i + 1)
                else:
                    length = len(heap)
                    if heap[length-1][1] > heap[1][1]:
                        del heap[length-1]
                    else:
                        swap(heap, 1, length-1)
                        del heap[length - 1]
                        bubbledown(heap, 1)
            return heap[1:]

        def sort(heap):
            heap = [[0, 0]] + heap
            length = len(heap)
            temp = []
            while len(heap) > 1:
                swap(heap, 1, len(heap) - 1)
                temp.append(heap[len(heap) - 1])
                del heap[len(heap) - 1]
                bubbledown(heap, 1)
            return temp

        if len(s) == 0:
            return ''
        else:
            heap = build(s, k)
            sorted_heap = sort(heap)

        return sorted_heap

    def frequencySort(self, s):
        map_dict = {}
        for i in s:
            map_dict[i] = map_dict.get(i, 0) + 1
        map_arr = [[i, j] for i, j in map_dict.items()]
        sorted_freq = self.heap_sort(s=map_arr)
        return ''.join([i * j for i, j in sorted_freq])

class Solution4(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = collections.defaultdict(int)
        for c in s:
            freq[c] += 1

        counts = [""] * (len(s)+1)
        for c in freq:
            counts[freq[c]] += c

        result = ""
        for count in reversed(range(len(counts)-1)):
            for c in counts[count]:
                result += c * count

        return result

if __name__ == '__main__':
    print(Solution4().frequencySort(s=''))
    print(Solution3().frequencySort(s="abaccadeeefaafcc"))