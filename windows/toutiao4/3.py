
"""
5 5 3
hello help high
p a b h m
f h e c p
o i l l h
b g h o n
h x c m l

"""

# from collections import defaultdict
#
#
# class Cell():
#     def __init__(self, value):
#         self.value = value
#         self.visited = False
#
#     def __str__(self):
#         return '{},{}'.format(self.value, self.visited)
#
#
# class Solution:
#     def build_trie(self, words):
#         dictionary = {}
#         char_count = defaultdict(int)
#         for i, word in enumerate(words):
#             d = dictionary
#             for char in word:
#                 if char not in d:
#                     d[char] = {}
#                 d = d[char]
#             d[1] = i
#             char_count[word[0]] += 1
#         return dictionary, char_count
#
#     def findWords(self, board, words):
#         """
#         :type board: List[List[str]]
#         :type words: List[str]
#         :rtype: List[str]
#         """
#         board_mem = defaultdict(list)
#         _board = []
#         # words = list(set(words))
#         nrow = len(board)
#         ncol = len(board[0])
#         # preprocess board
#         i, j = 0, 0
#         for i in range(nrow):
#             board_row = []
#             for j in range(ncol):
#                 board_mem[board[i][j]].append((i, j))
#                 board_row.append(Cell(board[i][j]))
#             _board.append(board_row)
#         trie_dic, char_count = self.build_trie(words)
#
#         def find_valid_neighbors(coord, dic):
#             i, j = coord[0], coord[1]
#             neighbor_coords = []
#             if i >= 1 and _board[i - 1][j].value in dic and not _board[i - 1][j].visited:
#                 neighbor_coords.append((i - 1, j))
#             if i < nrow - 1 and _board[i + 1][j].value in dic and not _board[i + 1][j].visited:
#                 neighbor_coords.append((i + 1, j))
#             if j >= 1 and _board[i][j - 1].value in dic and not _board[i][j - 1].visited:
#                 neighbor_coords.append((i, j - 1))
#             if j < ncol - 1 and _board[i][j + 1].value in dic and not _board[i][j + 1].visited:
#                 neighbor_coords.append((i, j + 1))
#             return neighbor_coords
#
#         def recursive_func(dic, coord):
#             if 1 in dic: result.add(words[dic[1]])
#             for (i, j) in find_valid_neighbors(coord, dic):
#                 _board[i][j].visited = True
#                 recursive_func(dic[_board[i][j].value], (i, j))
#                 _board[i][j].visited = False
#
#         result = set()
#         for first_c in trie_dic.keys():
#             prev_len = len(result)
#             for coord in board_mem[first_c]:
#                 _board[coord[0]][coord[1]].visited = True
#                 recursive_func(trie_dic[first_c], coord)
#                 _board[coord[0]][coord[1]].visited = False
#                 if len(result) - prev_len == char_count[first_c]: break  # found all chars
#         return list(result)



class Solution:
    def findWords(self, board, words):
        if not boards or not words:
            return []
        tries = {}
        for word in words:
            d = tries
            for ch in word:
                if ch not in d:
                    d[ch] = {}
                d = d[ch]
            d[1] = True
        # print(tries)
        M, N = len(board), len(board[0])
        if not M * N:
            return []
        self.res = []
        for i in range(M):
            for j in range(N):
                self.dfs(board, tries, i, j, "")
        return self.res

    def dfs(self, board, tree, i, j, prefix):
        if 1 in tree and prefix not in self.res:
            self.res.append(prefix)

        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] not in tree or board[i][j] == "*":
            return

        else:
            tmp = board[i][j]
            board[i][j] = "*"
            self.dfs(board, tree[tmp], i + 1, j, prefix + tmp)

            self.dfs(board, tree[tmp], i - 1, j, prefix + tmp)

            self.dfs(board, tree[tmp], i, j - 1, prefix + tmp)

            self.dfs(board, tree[tmp], i, j + 1, prefix + tmp)

            board[i][j] = tmp


m, n, k = list(map(int, input().strip().split()))
# print(m, n, k)
words = list(input().strip().split())
# print(words)
boards = []
for i in range(n):
    row = list(input().strip().split())
    boards.append(row)
# print(boards)

res = Solution().findWords(boards, words)
for item in res:
    print(item)
