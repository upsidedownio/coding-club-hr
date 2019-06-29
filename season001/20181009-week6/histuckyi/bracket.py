
# Complete the isBalanced function below.
"""
# len(s) == 0:
    returun 'YES'

# stack에는 left bracket만 들어간다.

while len(s) > 0:
    if s[0] == leftbracket:
        stack.append(s[0])
        s = s[1:]
    else:
        leftbracket = stack.pop()
        if leftbracket match s[0]:
            s = s[1:]
        else:
            return 'NO'

if len(stack) == 0:
    return "YES"
else:
    return 'NO'



"""
leftBracket = ['{', '[', '(']
rightBracket = ['}', ']', ')']

def matching(left, right):
    global leftBracket
    global rightBracket
    leftIndex = leftBracket.index(left)
    if rightBracket[leftIndex] == right:
        return True
    else:
        return False

def isBalanced(s):
    global leftBracket
    stack = []
    if len(s) == 0:
        return "YES"

    while len(s) > 0:
        bracket = s[0]
        if bracket in leftBracket:
            stack.append(bracket)
            s = s[1:]
        else:
            # "matching 할 left 요소가 없으면 error"
            if len(stack) == 0:
                return "NO"
            
            left = stack.pop()
            if matching(left, bracket):
                s = s[1:]
            else:
                return "NO"

    if len(stack) == 0:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    CaseList = [ "{[()]}", "{[(])}", "{{[[(())]]}}"]  # YES, NO, YES
    for s in CaseList:
        print(isBalanced(s))
