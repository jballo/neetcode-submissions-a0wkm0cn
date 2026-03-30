class Solution:
    def isValid(self, s: str) -> bool:
        # are we allowed to use other data structures?
        # am I allowed to use a python list ?
        # are there any space or time constraints?


        #match: stack and dictonary

        #plan
        # create an empty stack representing open notation
        openStack = []
        # create a dictionary [open notation, respective closed notation]
        closeDict = { '}': '{', ']': '[', ')': '('}

        # iterate through string s from 0 to last element
        for char in s:
            # # if s is closed notation
            if char in closeDict:
                # # # if true -> check the top element of s and check if its the appropriate element for the current closed notation
                if openStack and openStack[-1] == closeDict[char]:
                    # # # # if true, pop the top element from the stack
                    openStack.pop()
                else:
                    # # # # if false -> return False
                    return False
            else:
                # # if false, add current char to stack, continue to next character
                openStack.append(char)

        # check if the stack is not empty
        if len(openStack) != 0:
            # if not empty -> return False
            return False

        # return True
        return True
        