class Solution:
    def isValid(self, s: str) -> bool:
        
        # testcase1: s = "()[]{}"
        # char = "(" ⇨ stack["("]
        # char = ")" ⇨ stack[ ]
        # char = "[" ⇨ stack["["]
        # char = "]" ⇨ stack[ ]
        # char = "{" ⇨ stack["{"]
        # char = "}" ⇨ stack[ ]
        # return True
        
        # testcase2: s = "(]"
        # char = "(" ⇨ stack["("]
        # char = "]" ⇨ stack["(", "]"]
        # return False
        
        # cornercase: s is None
        if s is None:
            return False
        
        # step1: create dictionary
        dict = {')':'(', '}':'{', ']':'['}
        stack = []
        
        # step2: linear scan from left to right
        for char in s:
            if char in dict.values():
                stack.append(char)
            
            elif char in dict.keys():
                if dict[char] in stack:
                    stack.pop()
                else:
                    return False
            print(stack)
                
        return stack == []