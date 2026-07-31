class Solution:
    def isValid(self, s: str) -> bool:
        parenth = {')': '(', '}' : '{', ']':'['}
        stack = []
        for c in s:
            if c not in parenth:
                stack.append(c)
                continue
            if not stack or stack[-1] != parenth[c]:
                return False
            stack.pop()
        return not stack
