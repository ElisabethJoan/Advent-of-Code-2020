#DAY AGNOSTIC
def digestInput(fileName):
    with open(fileName) as file:
        lines = [line.strip() for line in file]
    return lines

#DAY 2
class Password:
    def __init__(self, lowerBound, upperBound, ruleChar, password):
        if lowerBound > upperBound:
            self.bounds = [upperBound, lowerBound]
            # self.range = range(upperBound, lowerBound + 1)
        else:
            self.bounds = [lowerBound, upperBound]
            # self.range = range(lowerBound, upperBound + 1)
        self.ruleChar = ruleChar
        self.password = password

def printClass(myClass):
    print(str(myClass.range) + " " + myClass.ruleChar + ": " + myClass.password)

def processInput(input):
    classList = []
    for line in input:
        temp = line.split()
        nums = temp[0].split("-")
        classList.append(Password(
            int(nums[0]),
            int(nums[1]),
            temp[1][0],
            temp[2]
        ))
    return classList


#DAY 3