class Solution:
    def convert(self, s: str, numRows: int) -> str:

        '''
        Parameters
        ----------
            s: str, numRows: int
        Returns
        -------
            str
            ⇨ return a string and make this conversion given a number of rows.
        '''

        row = 0
        res = [[] for _ in range(numRows)]
        direction = -1

        if numRows == 1 or numRows >= len(s):
            return s

        for char in s:
            res[row].append(char)
            if row == 0 or row == numRows-1:
                direction *= -1
            row += direction

        for i in range(len(res)):
            res[i] = ''.join(res[i])

        return ''.join(res)