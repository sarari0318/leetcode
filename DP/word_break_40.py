class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True

        return dp[-1]


'''
１回目のミス
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        word = s[0]
        index = 0

        for i in range(1, len(s) + 1):
            word = s[index:i]
            if word[:i] in wordDict:
                word = ''
                index = i
        return word == ''

⇨ 以下のケースに対応できず
"aaaaaaa"
["aaaa","aaa"]

部分ごとに毎にごとに見ていく必要がある
⇨ 二重ループで見る？
'''