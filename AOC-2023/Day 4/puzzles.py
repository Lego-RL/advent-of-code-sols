# with open("testinput.txt", "r") as f:
with open("input.txt", "r") as f:
# with open("AOC-2023/Day 4/testinput.txt", "r") as f:
    data = f.readlines()


data: list[str] = [x.strip("\n") for x in data]


def puzzle1():
    sumCards: int = 0
    
    for line in data:
        cardValue: int = 0
        # print(f"{line=}")
        
        # find value of card
        game: str = line[line.find(":")+2:]
        winningNums, myNums = game.split("|")
        winningNums, myNums = winningNums.strip(), myNums.split(" ")
        
        myNumsList = list(filter(lambda x: x != "", myNums))
        winningNumsList = list(filter(lambda x: x != "", winningNums.split(" ")))

        winningNumsList = list(map(lambda x: int(x.strip()), winningNumsList))
        myNumsList = list(map(lambda x: int(x.strip()), myNumsList))
        
        for num in myNumsList:
            # print("here")
            if num in winningNumsList:
                if cardValue == 0:
                    cardValue = 1
                else:
                    cardValue *= 2
                print(f"{cardValue=}")
        
        sumCards += cardValue
    
    print(sumCards)



def puzzle2():

    sumCards: int = 0
    totalScoreCards: int = 0
    scorecardCopies: map[int, int] = {}
    i: int = 0
    
    for line in data:
        i += 1
        if i not in scorecardCopies:
            scorecardCopies[i] = 1
        cardValue: int = 0
        
        # find value of card
        game: str = line[line.find(":")+2:]
        winningNums, myNums = game.split("|")
        winningNums, myNums = winningNums.strip(), myNums.split(" ")
        
        myNumsList = list(filter(lambda x: x != "", myNums))
        winningNumsList = list(filter(lambda x: x != "", winningNums.split(" ")))

        winningNumsList = list(map(lambda x: int(x.strip()), winningNumsList))
        myNumsList = list(map(lambda x: int(x.strip()), myNumsList))
        
        matchingNumCount: int = 0
        for num in myNumsList:
            if num in winningNumsList:
                matchingNumCount += 1
                if cardValue == 0:
                    cardValue = 1
                else:
                    # cardValue *= 2
                    cardValue += 1

        for j in range(i+1, i+matchingNumCount+1):
            if j > len(data):
                break
            
            copiesToAdd: int = 0
            if i in scorecardCopies:
                copiesToAdd = scorecardCopies[i]
            else:
                copiesToAdd = 1

            if j not in scorecardCopies:
                scorecardCopies[j] = copiesToAdd+1
                # print(f'added {copiesToAdd} to {j} on iteration {i}')
            else:
                scorecardCopies[j] = scorecardCopies[j] + copiesToAdd
                # print(f'added {copiesToAdd} to {j} on iteration {i}')

        
        sumCards += cardValue

    print(scorecardCopies)
    print(sum(list(scorecardCopies.values())))



if __name__ == "__main__":
    # puzzle1()
    puzzle2()