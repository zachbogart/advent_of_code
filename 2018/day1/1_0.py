total = 0

with open("input.txt") as file:
    for line in file:
        sign = line[0]
        value = int(line[1:])

        if sign == "+":
            total += value
        else:
            total -= value

print(total)