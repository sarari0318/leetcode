class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = {}
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