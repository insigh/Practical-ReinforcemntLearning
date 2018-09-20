'''
5
bytedance
toutiaohao
toutiaoapp
iesaweme
iestiktok
'''


def wordpre(words):
    tries = {}
    for word in words:
        d = tries
        for ch in word:
            if ch not in d:
                d[ch] = {}
                d[ch]['count'] = 1
            else:
                d[ch]['count'] += 1
            d = d[ch]
        # d[1] = True
    return tries


def find_pre(trie, words):
    for word in words:
        dict_tree = trie
        for i, ch in enumerate(word):
            if ch in dict_tree and dict_tree[ch]['count'] == 1:
                print(word[0:i+1])
                break
            else:
                dict_tree = dict_tree[ch]


n = int(input())
words = []
for i in range(n):
    words.append(input().strip())
# print(words)
print(wordpre(words))
find_pre(wordpre(words), words)
