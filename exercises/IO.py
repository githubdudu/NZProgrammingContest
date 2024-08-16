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