import sys

input = sys.argv[1]
output = ''
i = 0
while i < len(input):
    output += str(input[i])
    if i != len(input) - 1:
        output += str('\\r')
    i += 1
print(output)
