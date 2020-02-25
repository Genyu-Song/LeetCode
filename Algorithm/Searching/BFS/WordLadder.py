# -*- coding: UTF-8 -*-

'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
'''

import time
class Solution(object): # 超时
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        def find(word1, word2):
            word1, word2 = list(word1), list(word2)
            count = 0
            for letter1, letter2 in zip(word1, word2):
                if letter1 != letter2:
                    count += 1
                if count > 1:
                    return False
            return True

        wordList = set(wordList)
        search_list = []
        search_list.append(beginWord)
        known_result = {}
        known_result[beginWord] = 1
        while True:
            for word in search_list:
                for dic_word in wordList:
                    flag = find(word, dic_word)
                    if flag == True:
                        if not known_result.__contains__(dic_word):
                            known_result[dic_word] = known_result[word] + 1
                            if dic_word == endWord:
                                return known_result[dic_word]
                            else:
                                search_list.append(dic_word)
            try:
                return known_result[endWord]
            except:
                return 0

class Solution2(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def find(word1, word2):
            word1, word2 = list(word1), list(word2)
            count = 0
            for letter1, letter2 in zip(word1, word2):
                if letter1 != letter2:
                    count += 1
                if count > 1:
                    return False
            return True

        if endWord not in wordList:
            return 0

        search_list_front = []
        search_list_front.append(beginWord)
        search_list_back = []
        search_list_back.append(endWord)
        known_result_front = {}
        known_result_front[beginWord] = 1
        known_result_back = {}
        known_result_back[endWord] = 1
        while True:
            for word_front, word_back in zip(search_list_front, search_list_back):
                for dic_word in wordList:
                    flag_front = find(word_front, dic_word)
                    flag_back = find(word_back, dic_word)
                    if flag_front == True:
                        # if not known_result_front.__contains__(dic_word):
                        if dic_word not in known_result_front:
                            known_result_front[dic_word] = known_result_front[word_front] + 1
                            if dic_word == endWord:
                                return known_result_front[dic_word]
                            else:
                                search_list_front.append(dic_word)

                    if flag_back == True:
                        if dic_word not in known_result_back:
                            known_result_back[dic_word] = known_result_back[word_back] + 1
                            if dic_word == endWord:
                                return known_result_back[dic_word]
                            else:
                                search_list_back.append(dic_word)

                for mid_word in known_result_back:
                    if mid_word in known_result_front:
                        return known_result_front[mid_word] + known_result_back[mid_word] - 1
            try:
                return known_result_front[endWord]
            except:
                return 0

from collections import defaultdict
class Solution3(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)


        # Queue for BFS
        queue = [(beginWord, 1)]
        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.pop(0)
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]

                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0

if __name__ == '__main__':
    start = time.time()
    print(Solution2().ladderLength(beginWord = "hit",
                                  endWord = "cog",
                                  wordList = ["hot","dot","dog","lot","log","cog"]))
    print(time.time()-start)

