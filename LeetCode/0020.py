class Solution:
    '''
    Use a stack. When reached an open bracket, push it in. When reached a closed bracket, if the top item is the corresponding open bracket, pop the open bracket from the stack. 
    Time complexity: O(n), Space complexity: O(n). 
    '''
    def isValid(self, s: str) -> bool:
        pair = {')': '(', ']': '[', '}': '{'}
        st = []
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                st.append(ch)
            if ch == ')' or ch == ']' or ch == '}':
                if len(st) == 0 or st[-1] != pair[ch]: 
                    return False
                st.pop()
        return len(st) == 0
