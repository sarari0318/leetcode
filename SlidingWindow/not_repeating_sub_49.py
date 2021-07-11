class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        '''
        Parameters
        ----------
            s: str
        Returns
        -------
            int
            ⇨ return the length of the longest substring without repeating characters.
        '''

        # sの各要素のindexを記録
        seen = {}
        # countでsubstringの長さを記録
        count, last = 0, 0

        for i in range(len(s)):
            if s[i] not in seen.keys():
                count = max(count, i - last + 1)
            else:
                if seen[s[i]] < last:
                    count = max(count, i - last + 1)
                else:
                    last = seen[s[i]] + 1

            seen[s[i]] = i
        return count