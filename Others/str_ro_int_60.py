MAPPING = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "0": 0,
}

MAX_INT = 2**31-1
MIN_INT = -(2**31)

class Solution:
    def myAtoi(self, string):
        '''
        Parameters
        ----------
            string: str
            'string' consists of English letters (lower-case and upper-case),
                   digits (0-9), ' ', '+', '-', and '.'.
        Returns
        -------
            int
            ⇨ return the number included in string as integer.
        '''

        # stringの無駄なスペースを削除
        s = string.lstrip(' ')
        if not s:
            return 0

        # 正負を判別する変数
        sign = -1 if s[0] == "-" else 1

        if sign != 1 or s[0] == "+":
            s = s[1:]

        res = 0
        for char in s:
            if char not in MAPPING:
                return self.limit(res * sign)

            # 次の桁へ
            res *= 10
            res += MAPPING[char]

        return self.limit(res * sign)

    def limit(self, x: int) -> int:
        if x > MAX_INT:
            return MAX_INT
        if x < MIN_INT:
            return MIN_INT
        return x