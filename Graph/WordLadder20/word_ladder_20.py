import collections

class Solution:

    def ladderLength(self, beginWord, endWord, wordList):
        '''
        Parameters
        ----------
            beginWord: str
            endWord: str
            wordList: List[str]
        Returns
        -------
            int
            ⇨ return the number of words in the shortest transformation sequence from beginWord 
            to endWord, or 0 if no such sequence exists.
        '''

        # 各要素が固有になるように、set型に変換
        wordList = set(wordList)
        # 最初の要素を効率よく取り出せるように、dequeを用いる
        queue = collections.deque([[beginWord, 1]])

        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            # wordの１文字目から順に探索
            for i in range(len(word)):
                # アルファベットをaから順にword[i]に入れて単語を作ってみる
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])

        return 0