# 286. Walls and Gates

rooms = [
         [2147483647, -1, 0, 2147483647], 
         [2147483647, 2147483647, 2147483647, -1], 
         [2147483647, -1, 2147483647, -1], 
         [0, -1, 2147483647, 2147483647]
        ]
ans = [
        [3, -1, 0, 1],
        [2, 2, 1, -1],
        [1, -1, 2, -1],
        [0, -1, 3, 4]
      ]

# rooms = [[-1]]
# ans = [[-1]]

# Multi-Source BFS, T = O(ROWS * COLS), S = O(ROWS * COLS)
from collections import deque

ROWS, COLS = len(rooms), len(rooms[0])
visit = set()
q = deque()

for r in range(ROWS):
    for c in range(COLS):
        if rooms[r][c] == 0:
            q.append((r, c))
            visit.add((r, c))

def helper(r, c):
    if (r < 0 or r >= ROWS or c < 0 or c >= COLS or
        (r, c) in visit or rooms[r][c] == -1):
        return
    q.append((r, c))
    visit.add((r, c))

dist = 0

while q:
    for _ in range(len(q)):
        r, c = q.popleft()
        rooms[r][c] = dist

        helper(r + 1, c)
        helper(r - 1, c)
        helper(r, c + 1)
        helper(r, c - 1)

    dist += 1

print(rooms == ans)