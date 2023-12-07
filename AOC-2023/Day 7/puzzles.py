# with open("AOC-2023/Day 7/testinput.txt", "r") as f:
with open("AOC-2023/Day 7/input.txt", "r") as f:
    data = f.readlines()


data: list[str] = [x.strip("\n") for x in data]

cardStrengths: list[str] = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2", "1"]
cardStrengthsPartTwo: list[str] = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "1", "J"]
handTypes: list[str] = ["Five of a kind", "Four of a kind", "Full house", "Three of a kind", "Two pair", "One pair", "High card"]


class Hand():

    def __init__(self, hand: str, bid: int):
        self.hand = hand
        self.bid = bid

        #hand type for part 1
        # self.handType = self.getHandType(hand)
        self.handType = self.getHandTypePartTwo(hand)


    def __repr__(self):
        return f"{self.hand}: {self.handType}. {self.bid}"
    

    def __lt__(self, other) -> bool:
        if handTypes.index(other.handType) < handTypes.index(self.handType):
            return True
    
        elif handTypes.index(self.handType) < handTypes.index(other.handType):
            return False
         
        else:
            #they are equal so match based on each char
            for i in range(5):
                selfChar = self.hand[i]
                otherChar = other.hand[i]

                # if cardStrengths.index(otherChar) < cardStrengths.index(selfChar):
                if cardStrengthsPartTwo.index(otherChar) < cardStrengthsPartTwo.index(selfChar):
                    return True
            
                # elif cardStrengths.index(selfChar) < cardStrengths.index(otherChar):
                elif cardStrengthsPartTwo.index(selfChar) < cardStrengthsPartTwo.index(otherChar):
                    return False
                
                
                else:
                    continue



    def getHandType(self, hand: str) -> str:
        handSet: set[str] = set(hand)
        charCounts: dict[str, int] = {x:hand.count(x) for x in set(hand)}

        if len(handSet) == 1:
            # five of a kind for sure
            return handTypes[0]
        elif len(handSet) == 2:
            # four of a kind or full house
            if 4 in charCounts.values():
                # four of a kind if 4 of 1 number
                return handTypes[1]
            else:
                # full house if 3 & 2 of 2 numbers
                return handTypes[2]
        elif len(handSet) == 3:
            # three of a kind or two pair
            if 3 in charCounts.values():
                return handTypes[3]
            else:
                # must be two pair, 2 sets of 2 nums
                return handTypes[4]
        
        elif len(handSet) == 4:
            return handTypes[5]
        
        else:
            # high card, 5 diff nums
            return handTypes[6]
    

    def compareHandTypes(self, firstType, secondType) -> int:
        ## return 1 if firstType > secondType (better)
        ## return 0 if equal
        ## return -1 if firstType < secondType

        # lower index means better
        firstIndex = handTypes.index(firstType)
        secondIndex = handTypes.index(secondType)

        if firstIndex < secondIndex:
            return 1
        
        elif firstIndex > secondIndex:
            return -1
        
        else: 
            return 0
        


    def getHandTypePartTwo(self, hand: str) -> str:
        originalHandType = self.getHandType(hand)

        if "J" not in hand:
            return originalHandType
        
        else:
            # print("checking here")

            bestHandType: str = originalHandType
            # don't try replacing J with J, won't improve hand
            for cardType in cardStrengthsPartTwo[:-1]:
                # print(f"{cardType=}")
                testHand: str = hand
                testHand = testHand.replace("J", cardType)

                testHandType: str = self.getHandType(testHand)

                compareVal: int = self.compareHandTypes(testHandType, bestHandType)

                if compareVal == 1:
                    bestHandType = testHandType
                    # print(f"{bestHandType=}")

                # if best type already, return early
                if bestHandType == cardStrengths[0]:
                    return bestHandType
                
            return bestHandType

        
def puzzle1():
    hands: list[Hand] = []
    for line in data:
        info: list[str] = line.split(" ")
        hands.append(Hand(info[0], int(info[1])))

    hands.sort()

    sum: int = 0
    for i, hand in enumerate(hands):
        handScore: int = hand.bid * (i+1)
        sum += handScore

    print(sum)



def puzzle2():
    hands: list[Hand] = []
    for line in data:
        info: list[str] = line.split(" ")
        hands.append(Hand(info[0], int(info[1])))

    hands.sort()

    sum: int = 0
    for i, hand in enumerate(hands):
        handScore: int = hand.bid * (i+1)
        sum += handScore

    print(sum)


if __name__ == "__main__":
    # puzzle1()
    puzzle2()