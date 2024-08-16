"""
RO2E
BD2F
BO3F
GO3F
GD2S
RO3F
RS2F
RO1E
RD3S
GO1S
BO2S
BO2E
Output for Sample Input
1 3 10 346
4 8 11 5 7 12 6 10 12
789
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
    def strTuple(self, tuple):
        return "%s %s" % tuple
    def strList(self, li):
        return " ".join(map(str, li))
io = IO()

inputs = []
for i in range(12):
    inputs.append(io.getStr())

def match(ach, bch, cch):
    if ach == bch and ach == cch:
        return True
    elif ach != bch and ach != cch and bch != cch:
        return True
    return False

def isSet(x, y, z):
    for i in range(4):
        if not match(x[i], y[i], z[i]):
            return False
    return True


output = []
for first in range(12):
    for second in range(first + 1, 12):
        for third in range(second + 1, 12):
            if(isSet(inputs[first], inputs[second], inputs[third])):
                output.append((first + 1, second + 1, third + 1))

for o in output:
    print(io.strList(o))