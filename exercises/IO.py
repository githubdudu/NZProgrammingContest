class IO():
    def getStr():
        return input()
    
    def getInt():
        return int(input())
    
    def getStrList():
        return input().split(' ')

    def getIntList():
        return [int(x) for x in input().split(' ')]
    
io = IO()