s = "racecar"
t = "carrace"
ans = True

# s = "jar"
# t = "jam"
# ans = False

# s = "x"
# t = "x"
# ans = True

from collections import Counter
from collections import defaultdict

mapS = defaultdict(int)
mapT = defaultdict(int)

for i in range(len(s)):
    mapS[s[i]] += 1
    mapT[t[i]] += 1

print(mapS == mapT)

print(ans == (Counter(s) == Counter(t)))