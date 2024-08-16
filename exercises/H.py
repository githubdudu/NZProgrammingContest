


"""
20 100 
6 100 
11 
G 4 
R 6 
G 3 
R 8 
G 5 
R 6 
G 4 
R 5 
G 5 
R 3 
G 5

output

Longest queue was 15 vehicles. 
Longest through time was 5 minutes and 40 seconds. 
 

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


def addTime(li, value):
    return map(lambda x: x + value, li)

def H():
    # 2 line of input
    greenTimes, redTimes = io.getIntList()
    numOfCars, endTime = io.getIntList()

    # the output
    maxCars, maxTime = numOfCars, endTime

    queue = [endTime] * numOfCars

    numberOfSeq = io.getInt()

    for _ in range(numberOfSeq):
        line = io.getStrList()
        type, numOfNewCars = line[0], int(line[1])

        if type == 'G':
            for i in range(numOfNewCars):
                startTime = queue.pop(0)
                maxTime = max(maxTime, endTime - startTime)

            endTime += greenTimes
        else:
            for i in range(numOfNewCars):
                queue.append(endTime)
            maxCars = max(maxCars, len(queue))
            endTime += redTimes

    return maxCars, maxTime

maxCars, maxTime = H()
print(f"Longest queue was {maxCars} vehicles.") 
print("Longest through time was %1d minutes and %1d seconds." % ((maxTime - maxTime % 60)/ 60, maxTime % 60))