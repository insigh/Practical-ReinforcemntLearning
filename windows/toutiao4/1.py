def simplifyPath(path):
    """
    :type path: str
    :rtype: str
    """

    path = path.split('/')
    # print(path)
    res = '/'
    stack = []
    for item in path:
        if item == '' or item == '.' or (item == '..' and not stack):
            continue
        elif item == '..':
            stack.pop(-1)
        else:
            stack.append(item)
    # print(stack)
    return res + '/'.join(stack)


input = input().strip()
# print(input)
print(simplifyPath(input))
