n = int(input())

list = ["Ruby", "jo", "fiona", "Phoebe", "Angela", "Sophia"]

def swap(_from, _to):
    temp = list[_from]
    list[_from] = list[_to]
    list[_to] = temp

for i in range(n):
    _from, _to = input().split(" ")
    swap(int(_from) - 1, int(_to) - 1)

print(list)