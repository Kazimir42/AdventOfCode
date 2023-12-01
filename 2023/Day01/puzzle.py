import re

# Load input
with open('input.txt') as f:
    lines = f.readlines()

total = 0
for line in lines:
    # Find first input with regex
    firstNumber = re.search("[0-9]", line).group()

    # Inverse
    lastNumber = re.search("[0-9]", line[::-1]).group()

    result = int(firstNumber + lastNumber)
    total += result

# Result
print(total)
