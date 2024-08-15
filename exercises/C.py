"""

Bottom left: 0, 0
Top right: 14, 4

0 <= y <= 4
0 <= x <= 14
5 <= N <= 500
"""

class IO():
    def getStr(self):
        return input().strip()
    
    def getInt(self):
        return int(input())
    
    def getStrList(self):
        return self.getStr().split(' ')

    def getIntList(self):
        return [int(x) for x in self.getStrList()]
    
io = IO()

N = io.getInt()
print(N)
hash = {}

def getScore(symbol):
    if symbol == 'S':
        return -1
    else:
        return 1
    
for i in range(N):
    sss = io.getStrList()
    print(sss)
    symbol, corX, corY = sss[0], sss[1], sss[2]
    corX, corY = int(corX), int(corY)
    cor = (corX, corY)
    if(symbol == 'M'):
        continue

    if cor in hash:
        hash[cor] += getScore(symbol)
    else:
        hash[cor] = getScore(symbol)

list = [item for item in sorted(hash.items(), key=lambda pair: pair[1])]

maxScore = list[-1][1]
output = "Best place "

list = [k for k, v in list if v == maxScore]

list = [str(k[0]) + " " + str(k[1]) for k in sorted(list, key=lambda cor: cor[0])]

output += ", ".join(list)
print(output + '.')