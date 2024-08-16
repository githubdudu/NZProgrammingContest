


"""
6 
1 1 2 2 2 3

Output:
3
1 2
1 2
2 3
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

# input
N = io.getInt();
boxes = io.getIntList();
boxes.sort();

# init
solution = []

def insert(list, index, item):
    if len(list) - 1 < index:
        list.append([item]);
    elif list[index][-1] >= item:
        insert(list, index + 1, item);
    else:
        list[index].append(item)

def I():
    for box in boxes:
        insert(solution, 0, box);


    # output
    print(len(solution));
    for s in solution:
        print(io.strList(s))


I()
