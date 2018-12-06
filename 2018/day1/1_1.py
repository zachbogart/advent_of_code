def find_double():

    input = []
    history = {}
    total = 0
    round = 1

    with open("input.txt") as file:
        for line in file:
            sign = line[0]
            value = int(line[1:])

            if sign == "+":
                input.append(value)
            else:
                input.append(value * -1)

    while True:
        for item in input:
            total += item
            if str(total) in history:
                print("{} repeated twice after {} rounds".format(total, round))
                return
            else:
                history[str(total)] = total
        round += 1

find_double()