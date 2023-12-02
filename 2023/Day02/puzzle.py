import re

# Load input
with open('input.txt') as f:
    lines = f.readlines()

# Define variables
bag = {'red': 12, 'green': 13, 'blue': 14}
total = 0

for line in lines:
    # Define line variable
    isPossible = True

    # Get game id
    gameId = re.search('Game (\d+)', line).group(1)

    # Clean string
    line = line[(line.find(':') + 2):]

    # Create array of sets
    sets = line.split(';')
    for set in sets:
        # Construct object
        colors = {'red': 0, 'green': 0, 'blue': 0}

        red = re.search('(\d+)\s+red', set)
        if red is not None:
            colors['red'] = int(red.group(1))

        green = re.search('(\d+)\s+green', set)
        if green is not None:
            colors['green'] = int(green.group(1))

        blue = re.search('(\d+)\s+blue', set)
        if blue is not None:
            colors['blue'] = int(blue.group(1))

        # Check if not possible
        if bag['red'] < colors['red'] or bag['green'] < colors['green'] or bag['blue'] < colors['blue']:
            isPossible = False

    if isPossible is True:
        total += int(gameId)

# Result
print(total)
