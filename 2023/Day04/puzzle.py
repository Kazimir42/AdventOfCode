# Load input
with open('input.txt') as f:
    lines = f.readlines()

# Define variables
total = 0

for lineIndex, line in enumerate(lines):
    # Clean string
    line = line[(line.find(':') + 2):]
    line = line.strip()
    lines = line.split('|')
    leftNumbers = lines[0].split(' ')
    leftNumbers = list(filter(None, leftNumbers))
    rightNumbers = lines[1].split(' ')
    rightNumbers = list(filter(None, rightNumbers))

    result = 0
    for leftNumber in leftNumbers:
        if leftNumber in rightNumbers:
            if result == 0:
                result = 1
            else:
                result = result * 2

    total += result

# Result
print(total)
