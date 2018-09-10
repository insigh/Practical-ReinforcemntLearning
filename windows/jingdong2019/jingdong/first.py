def  solve(s='abcc', t='xyaa'):
    lt = len(t)
    count = 0
    for i in range(0, len(s)-len(t)+1):
        s_ = s[i:i+len(t)]
        if get_style(s_) == get_style(t):
            count += 1
    return count



def get_style(s):
    dict_ = {}
    for i, ch in enumerate(s):
        if ch in dict_.keys():
            dict_[ch] += 1
        else:
            dict_[ch] = 1
    template = []
    for i, ch in enumerate(s):
        template.append(dict_[ch])
    return template



print(solve())

