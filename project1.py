import random


class ListOfRandomIntegers:
    sequence = []
    LENGTH = None
    UPPER = None
    LOWER = None

    def __init__(self):
        '''
            Initialises ListOfRandomIntegers.

            Params:
                None

            Returns:
                None
        '''
        pass

    def setLength(self):
        '''
            Asks user for desired length of list and sets self.LENGTH to that value.

            Params:
                None
            
            Returns:
                None
        '''
        while True:
            length = input("Please enter the length for the list:\t")
            try:
                self.LENGTH = int(length)
                if self.LENGTH <= 0:
                    print(
                        "Value given cannot be less than or equal to zero, please try again")
                    continue
                break
            except ValueError:
                print("Value given is not correct, please try again")
        return None

    def setUpper(self):
        '''
            Asks user for desired upper bound list and sets self.UPPER to that value.

            Params:
                None
            
            Returns:
                None
        '''
        while True:
            upper = input(
                "Please enter the upper bound for the range of integer values:\t")
            try:
                self.UPPER = int(upper)
                if self.LOWER is not None:
                    if self.UPPER <= self.LOWER:
                        print(
                            "Upper bound is lesser than or equal to lower bounds, please try again")
                        continue
                break
            except ValueError:
                print("Value given is not correct, please try again")
        return None

    def setLower(self):
        '''
            Asks user for desired lower bound of list and sets self.LOWER to that value.

            Params:
                None
            
            Returns:
                None
        '''
        while True:
            lower = input(
                "Please enter the lower bound for the range of integer values:\t")
            try:
                self.LOWER = int(lower)
                if self.UPPER is not None:
                    if self.LOWER >= self.UPPER:
                        print(
                            "Lower bound is greater than or equal to upper bound, please try again")
                        continue
                break
            except ValueError:
                print("Value given is not correct, please try again")
        return None

    def generateSequence(self):
        '''
            Generates sequence given self.LOWER, self.UPPER and self.LENGTH.

            Params:
                None
            
            Returns:
                None
        '''
        self.sequence = []
        for _ in range(self.LENGTH):
            self.sequence.append(random.randrange(self.LOWER, self.UPPER))
        print("\nSequence: {}\n".format(str(self.sequence)))
        return None

    def getLength(self):
        '''
            Returns length of generated sequence.

            Params:
                None
            
            Returns:
                Integer - length of generated sequence.
        '''
        return len(self.sequence)

    def getSmallest(self):
        '''
            Returns smallest integer in generated sequence.

            Params:
                None
            
            Returns:
                Integer - smallest integer of generated sequence.
        '''
        return min(self.sequence)

    def getLargest(self):
        '''
            Returns largest integer in generated sequence.

            Params:
                None
            
            Returns:
                Integer - largest integer of generated sequence.
        '''
        return max(self.sequence)

    def getSum(self):
        '''
            Returns sum of all integers in generated sequence.

            Params:
                None
            
            Returns:
                Integer - sum of all integers in generated sequence.
        '''
        return sum(self.sequence)

    def getAverage(self):
        '''
            Returns arithmetic mean of all integers in generate sequence.

            Params:
                None
            
            Returns:
                Float - arithmetic mean of all integers in generate sequence.
        '''
        return self.getSum()/self.getLength()

    def printStats(self):
        '''
            Prints formatted summary numbers of generated sequence.

            Params:
                None

            Returns:
                None
        '''
        print("List length: {}".format(self.getLength()))
        print("Largest integer: {}".format(self.getLargest()))
        print("Smallest integer: {}".format(self.getSmallest()))
        print("Sum: {}".format(self.getSum()))
        print("Average: {}".format(self.getAverage()))


if __name__ == "__main__":
    l = ListOfRandomIntegers()
    l.setLength()
    l.setLower()
    l.setUpper()
    l.generateSequence()
    l.printStats()
