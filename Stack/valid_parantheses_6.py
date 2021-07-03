class Solution:
    def isValid(self, s: str) -> bool:
              
        '''
        Parameters
        ----------
            s: str
        Returns
        -------
            bool
            ⇨ determine if the input string is valid.

            valid input example: "()", "()[]{}", "{[]}"
            invalid input example: "(]", "([)]"
        '''
        
        # Parenthesesの対照表
        parent_table = {')':'(', '}':'{', ']':'['}
        stack = []
        
        for char in s:
            # もしcharが左側の括弧である時、
            if char in parent_table.values():
                stack.append(char)
            
            # もしcharが右側の括弧である時、
            else:
                # stackが空
                # もしくは 
                # stackの最後の要素が charに対応する左側の括弧でなければ、
                if stack == [] or parent_table[char] != stack.pop():
                    return False     
        return stack == []