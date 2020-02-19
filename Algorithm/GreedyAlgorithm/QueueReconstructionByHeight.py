# -*- coding: UTF-8 -*-

'''
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.
'''

class Solution(object): # Ascending order
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda x:x[0])
        new_list = [[-1, -1] for i in range(len(people))]
        for h, k in people:
            count = 0
            ind = 0
            while count != k:
                if new_list[ind][0] >= h or new_list[ind][0] == -1:
                    count += 1
                ind += 1
            while new_list[ind][0] != -1:
                ind += 1
            new_list[ind] = [h, k]
        return new_list

class Solution2(object): # Descending order
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda x: (-x[0], x[1])) # TODO: 注意排序写法people.sort(key=lambda x: x[0], reverse=True)错在哪儿！
        new_list = []
        for h, k in people:
            new_list.insert(k, (h, k)) # insert() takes no keyword arguments, 不支持用键值对传参
        return new_list


if __name__ == '__main__':
    print(Solution2().reconstructQueue(people=[[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]))