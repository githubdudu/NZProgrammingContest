
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
answer = io.getStr()
round = 0
while True:
    bulls, cows = 0, 0
    round += 1

    line = io.getStr()
    if line == "GIVE UP": 
        print(f'The word was not guessed. Answer: {answer}.')
        break

    for letter in line:
        if letter in answer:
            cows += 1
    for i in range(len(line)):
        if line[i] == answer[i]:
            bulls += 1

    cows -= bulls
    print(f"{line} Score {bulls} bulls and {cows} cows.")
    
    if bulls == 4:
        print(f"The word was guessed in {round}.")
        break
