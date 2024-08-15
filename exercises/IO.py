class IO():
    def getStr(self):
        return input()
    
    def getInt(self):
        return int(input())
    
    def getStrList(self):
        return input().split(' ')

    def getIntList(self):
        return [int(x) for x in input().split(' ')]
    
io = IO()