from aoc2020lib import digestInput, d4processInput

input = digestInput("day4input.txt")
requiredDelims = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
byr = range(1920, 2003)
iyr = range(2010, 2021)
eyr = range(2020, 2031)
hgtcm = range(150, 194)
hgtin = range(59, 77)
hcl = "#"
hcls = "1234567890abcdef"
ecl = set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])

def solution():
    passports = d4processInput(input)
    counter = 0
    for i in passports:
        if requiredDelims.issubset(i.keys()):
            if int(i["byr"]) in byr and int(i["iyr"]) in iyr and int(i["eyr"]) in eyr:
                if (i["hgt"][-2:] == "cm" and int(i["hgt"][:-2]) in hgtcm) or (i["hgt"][-2:] == "in" and  int(i["hgt"][:-2]) in hgtin):
                    if i["hcl"][0] == hcl and len(i["hcl"][1:]) == 6:
                        match = [str(x) in hcls for x in i["hcl"][1:]]
                        if i["ecl"] in ecl and all(match) and len(i["pid"]) == 9:
                            try:
                                int(i["pid"])
                                counter += 1
                            except:
                                continue
    return counter

x = solution()
print(x)