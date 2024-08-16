class IO():
    def getStr(self):
        return input().strip()
    def getInt(self):
        return int(input())
    def getStrList(self):
        return self.getStr().split(' ')
    def getIntList(self):
        return [int(x) for x in self.getStrList()]
    def strTuple(tuple):
        return "%s %s" % tuple
    def strList(li):
        return " ".join(map(str, li))
io = IO()
"""
10  
Ngata  
Li  
Brown  
Li  
Li  
Ngata  
Brown  
Li  
Li  
Brown  
  
Output for Sample Input 1  
 
Li won by 2 votes.
"""

N = io.getInt()
boxes = {}
for n in range(N):
    name = io.getStr()
    if name in boxes:
        boxes[name] += 1
    else:
        boxes[name] = 1

result = sorted(boxes.items(), key=lambda x: (-x[1], x[0]))
if len(result) == 1:
    print(f"{result[0][0]} won by {result[0][1]} {"notes" if result[0][1] > 1 else "note"}.")

if result[0][1] == result[1][1]:
    names = []
    for re in result:
        if re[1] != result[0][1]:
            break
        names.append(re[0])

    print(f"Tie between {", ".join(names)}.")
else:
    diff = result[0][1] - result[1][1]
    print(f"{result[0][0]} won by {diff} {"notes" if result[0][1] > 1 else "note"}.")
