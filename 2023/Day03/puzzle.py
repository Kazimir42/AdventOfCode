import re

# Load input
with open('input.txt') as f:
    lines = f.readlines()

# Define variables
total = 0


# Functions

def has_adjacent_special_char(lines, lineIndex, positions):
    linesToSearch = []

    if lineIndex > 0:
        linesToSearch.append(lines[lineIndex - 1])

    linesToSearch.append(lines[lineIndex])

    if lineIndex < len(lines) - 1:
        linesToSearch.append(lines[lineIndex + 1])

    positions = list(range(positions[0] - 1, positions[-1] + 2))

    for lineIndex, line in enumerate(linesToSearch):
        for position in positions:
            ## Spent 20 minutes cuz i forgot to add /n in my REGEX zzzzzzzzzz
            if re.search('[^0-9a-zA-Z^.\n]+', line[position]):
                return True

    return False


for lineIndex, line in enumerate(lines):
    for regexResult in re.finditer('(\d+)', line):
        numberFind = regexResult.group()
        numberStartPosition = regexResult.start()
        numberEndPosition = regexResult.end()
        numberZone = list(range(numberStartPosition, numberEndPosition))

        result = has_adjacent_special_char(lines, lineIndex, numberZone)
        if result is True:
            total += int(numberFind)

# Result
print(total)
