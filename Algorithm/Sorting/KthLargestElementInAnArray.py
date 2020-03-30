# -*- coding: UTF-8 -*-

'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
'''

from random import randint

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

    def findKthLargest(self, nums, k):
        self.nums = nums
        self.k = k
        self.data_list = [0]
        for i in self.nums:
            if len(self.data_list) < self.k + 1:
                self.__floatup(i)
            else:
                self.__bubbledown(i)
        return self.data_list[1]

class QuickSort(object):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    Quick sort —— Partition
    TODO: NEXT TIME !
    """

    def swap(self, index1, index2):
        self.nums[index1], self.nums[index2] = self.nums[index2], self.nums[index1]

    def get_pivot(self, first, last):
        '''
        TODO: Attention
        '''
        mid = (first + last) // 2
        pivot = last
        if self.nums[first] < self.nums[mid]:
            if self.nums[mid] > self.nums[last]:
                pivot = mid
        elif self.nums[first] < self.nums[last]:
            pivot = first
        return pivot

    # def get_pivot(self, i, j):
    #     m = j - (i + j) // 2
    #     pivot = m
    #     if self.nums[i] >= self.nums[j]:
    #         if self.nums[m] >= self.nums[i]:
    #             pivot = i
    #         elif self.nums[m] <= self.nums[j]:
    #             pivot = j
    #     elif self.nums[j] >= self.nums[i]:
    #         if self.nums[m] >= self.nums[j]:
    #             pivot = j
    #         elif self.nums[m] <= self.nums[i]:
    #             pivot = i
    #     return pivot

    def partition(self, left, right, pivot):
        if left == right:
            return left
        if right - left == 1:
            if self.nums[left] > self.nums[right]:
                self.swap(left, right)
                return right
        self.swap(left, pivot)
        border = left + 1
        for i in range(left + 2, right + 1):
            if self.nums[i] < self.nums[left]:
                self.swap(i, border)
                if i != right:
                    border += 1
        self.swap(left, border)
        return border

    def findKthLargest(self, nums, k):
        self.nums = nums
        self.k = k
        left, right = 0, len(self.nums) - 1
        # while store_index != len(self.nums) - k:
        while left <= right:
            pivot = self.get_pivot(left, right)
            store_index = self.partition(left, right, pivot)
            if store_index > len(nums) - k:
                right = store_index - 1
            elif store_index < len(nums) - k:
                left = store_index + 1
            elif store_index == len(nums) - k:
                return nums[store_index]

from typing import List
class Solutionxx:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        def get_pivot(l, r):
            m = r - (l + r) // 2
            tmp = [nums[l], nums[m], nums[r]]
            tmp.sort()
            if tmp[1] == nums[l]:
                return l
            elif tmp[1] == nums[r]:
                return r
            return m

        def partition(l, r):
            pivot_ind = get_pivot(l, r)
            pivot_val = nums[pivot_ind]
            swap(pivot_ind, l)
            border = l
            for i in range(l + 1, r + 1):
                if nums[i] < pivot_val:
                    border += 1
                    swap(border, i)
            swap(l, border)
            return border

        l, r = 0, len(nums) - 1
        target = len(nums) - k
        while True:
            index = partition(l, r)
            if index == target:
                return nums[index]
            elif index > target:
                r = index - 1
            else:
                l = index + 1

if __name__ == '__main__':
    print(Solutionxx().findKthLargest(nums=[3,2,3,1,2,4,5,5,6], k=4))

    print(heapify().findKthLargest(nums=[3,2,3,1,2,4,5,5,6], k=9))

    print(QuickSort().findKthLargest(nums=[3,3,3,3,4,3,3,3,3], k=1))