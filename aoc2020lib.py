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


#DAY 4
def d4processInput(input):
    coutner = 0
    passports = []
    tempDict = {}
    for i in range(len(input)):
        if input[i] == "" or i + 1 == len(input):
            passports.append(tempDict)
            if i + 1 == len(input):
                tempDict.update(dict(x.split(":") for x in input[i].split(" ")))
            tempDict = {}
            continue
        tempDict.update(dict(x.split(":") for x in input[i].split(" ")))
    return passports