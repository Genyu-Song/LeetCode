# -*- coding: UTF-8 -*-

'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
'''

class Solution(object):
    def method1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums, reverse=True)
        return nums[k-1]

    def method2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        TODO:
        Bit Manipulation: >>, <<
        Minimum Heap for sorting.
        """
        KList = [0]
        for i in nums:
            KList.append(i)
            index = len(KList) - 1
            parent_index = index >> 1
            if len(KList) < k + 2:
                while parent_index is not None and KList[index] < KList[parent_index]:
                    if parent_index == 0:
                        break
                    KList[index], KList[parent_index] = KList[parent_index], KList[index]
                    index = parent_index
                    parent_index = parent_index >> 1
            else:
                if KList[1] < KList[index]:
                    KList[1], KList[index] = KList[index], KList[1]
                del KList[-1]
                index = 1
                while True:
                    minvalue_index = index
                    if 2 * index <= k and KList[2 * index] < KList[minvalue_index]:
                        minvalue_index = 2 * index
                    if 2 * index + 1 <= k and KList[2 * index + 1] < KList[minvalue_index]:
                        minvalue_index = 2 * index + 1
                    if minvalue_index == index:
                        break
                    KList[index], KList[minvalue_index] = KList[minvalue_index], KList[index]
                    index = minvalue_index
        return KList[1]

class heapify(object):
    def __swap(self, index1, index2):
        self.data_list[index1], self.data_list[index2] = self.data_list[index2], self.data_list[index1]

    def __floatup(self, data):
        self.data_list.append(data)
        index = len(self.data_list) - 1
        parent_index = index >> 1
        while True:
            if parent_index < 1 or parent_index is None or len(self.data_list) == 2:
                return
            elif self.data_list[index] < self.data_list[parent_index]:
                self.__swap(index, parent_index)
            index = parent_index
            parent_index = index >> 1

    def __bubbledown(self, data):
        self.data_list.append(data)
        last_index = len(self.data_list) - 1
        if self.data_list[1] < self.data_list[last_index]:
            self.__swap(1, last_index)
        del self.data_list[last_index]
        index = 1
        k = self.k
        while True:
            min_index = index
            left, right = min_index * 2, min_index * 2 + 1
            if left <= k and self.data_list[left] < self.data_list[min_index]:
                min_index = left
            if right <= k and self.data_list[right] < self.data_list[min_index]:
                min_index = right
            if min_index == index:
                break
            self.__swap(index, min_index)
            index = min_index

    def klargest(self, nums, k):
        self.nums = nums
        self.k = k
        self.data_list = [0]
        for i in self.nums:
            if len(self.data_list) < self.k + 1:
                self.__floatup(i)
            else:
                self.__bubbledown(i)
        return self.data_list[1]

if __name__ == '__main__':
    print(Solution().method2(nums=[3,2,1,5,6,4], k=2))

    print(heapify().klargest(nums=[3,2,3,1,2,4,5,5,6], k=9))