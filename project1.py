import random

class List_of_Random_Integers:
    SEQUENCE = []
    LENGTH = None
    UPPER = None
    LOWER = None

    def __init__(self):
        pass

    def setLength(self):
        while True:
            length = input("Please enter the length for the list:\t")
            try:
                self.LENGTH = int(length)
                if self.LENGTH <= 0:
                    print("Value given cannot be less than or equal to zero, please try again")
                    continue
                break
            except ValueError:
                print("Value given is not correct, please try again")
        return None

    def setUpper(self):
        while True:
            upper = input("Please enter the upper bound for the range of integer values:\t")
            try:
                self.UPPER = int(upper)
                if self.LOWER is not None:
                    if self.UPPER <= self.LOWER:
                        print("Upper bound is lesser than or equal to lower bounds, please try again")
                        continue
                break
            except ValueError:
                print("Value given is not correct, please try again")
        return None

    def setLower(self):
        while True:
            lower = input("Please enter the lower bound for the range of integer values:\t")
            try:
                self.LOWER = int(lower)
                if self.UPPER is not None:
                    if self.LOWER >= self.UPPER:
                        print("Lower bound is greater than or equal to upper bound, please try again")
                        continue
                break
            except ValueError:
                print("Value given is not correct, please try again")
        return None

    def generateSequence(self):
        for _ in range(self.LENGTH):
            self.SEQUENCE.append(random.randrange(self.LOWER, self.UPPER))
        print("Sequence: {}".format(str(self.SEQUENCE)))
        return None

    def getLength(self):
        return len(self.SEQUENCE)

    def getSmallest(self):
        return min(self.SEQUENCE)

    def getLargest(self):
        return max(self.SEQUENCE)

    def getSum(self):
        return sum(self.SEQUENCE)

    def getAverage(self):
        return self.getSum()/self.getLength()
    
    def printStats(self):
        print("List length: {}".format(self.getLength()))
        print("Largest integer: {}".format(self.getLargest()))
        print("Smallest integer: {}".format(self.getSmallest()))
        print("Sum: {}".format(self.getSum()))
        print("Average: {}".format(self.getAverage()))

if __name__ == "__main__":
    l = List_of_Random_Integers()
    l.setLength()
    l.setLower()
    l.setUpper()
    print("")
    l.generateSequence()
    print("")
    l.printStats()

