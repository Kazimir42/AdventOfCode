# Load input
import re

with open('input.txt') as f:
    lines = f.readlines()

# Define variables
currentPosition = 'AAA'
directions = lines[0].replace('L', '0').replace('R', '1').strip()

inputArray = {}

# Deletes directions string and blank line
del lines[0]
del lines[0]

# Create array with input
for lineIndex, line in enumerate(lines):
    inputArray[re.findall('([A-Z][A-Z][A-Z])', line)[0]] = [re.findall('([A-Z][A-Z][A-Z])', line)[1],
                                                            re.findall('([A-Z][A-Z][A-Z])', line)[2]]


def find_zzz(_currentPosition, _directions, _inputArray, _step):
    for index, direction in enumerate(_directions):
        element = _inputArray[_currentPosition][int(direction)]
        _currentPosition = element
        _step = _step + 1
        if element == 'ZZZ':
            return _step

        # We are at the end of for without find ZZZ
        if (index + 1) == len(directions):
            return find_zzz(_currentPosition, _directions, _inputArray, _step)


print(find_zzz(currentPosition, directions, inputArray, 0))


