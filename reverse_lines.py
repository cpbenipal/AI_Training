with open('input.txt', 'r') as file:
    lines = file.readlines()

with open('output.txt', 'w') as file:
    for line in reversed(lines):
        file.write(line)
