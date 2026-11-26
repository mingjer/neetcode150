# 39. Combination Sum

# candidates = [2, 3, 6, 7]
# target = 7
# ans = [[2, 2, 3], [7]]

candidates = [2, 3, 5]
target = 8
ans = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

# candidates = [2]
# target = 1
# ans = []


# backtracking
res = []

def dfs(i, cur, total):
    # base case, when to 
    if total == target:
        res.append(cur.copy())
        return
    if i >= len(candidates) or total > target:
        return 

    # include itself
    cur.append(candidates[i])
    dfs(i, cur, total + candidates[i])

    cur.pop()
    dfs(i + 1, cur, total)

dfs(0, [], 0)

print(res == ans)