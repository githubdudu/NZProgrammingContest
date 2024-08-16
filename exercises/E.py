
# Sample Input
# S3(TR)3SL
# Output for Sample Input
# STRTRTRSSSL
# 4 3 3 1

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

def E():
    times = 1
    inBracket = False
    output = ''
    subStr = ''

    beads = io.getStr()
    
    for bead in reversed(beads):
        if bead.isnumeric():
            output += subStr * int(bead)
            subStr = ''
        elif bead == '(':
            inBracket = False
        elif bead == ')':
            inBracket = True
        else:
            if not inBracket:
                output += subStr
                subStr = bead
            else:
                subStr += bead
    output += subStr
    return output[::-1]

def countNumber(outputs):
    counts = [0, 0, 0, 0]
    for bead in outputs:
        if bead == "S":
            counts[0] += 1
        elif bead == "T":
            counts[1] += 1
        elif bead == "R":
            counts[2] += 1
        elif bead == "L":
            counts[3] += 1
    return io.strList(counts)

output = E()
print(output)
count = countNumber(output)
print(count)