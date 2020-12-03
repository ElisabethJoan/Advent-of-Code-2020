def digestInput(fileName):
    with open(fileName) as file:
        lines = [int(line.strip()) for line in file]
    return lines
