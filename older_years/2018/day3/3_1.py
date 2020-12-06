import numpy as np
import re

def get_input_text_array():

    input = []

    with open("input.txt") as file:
        for line in file:
            input.append(line[:-1])

    return input

def add_to_claims(claims, x, y, w, h):
    for ind_x in range(x, x + w):
        for ind_y in range(y, y + h):
            claims[ind_x][ind_y] += 1

def add_claim_overlaps(input_array, claims):
    for line in input_array:
        line = re.sub('[#@:]', '', line)
        line = re.sub('[,x]', ' ', line)
        params = line.split(' ')

        x = int(params[2])
        y = int(params[3])
        w = int(params[4])
        h = int(params[5])

        add_to_claims(claims, x, y, w, h)

def get_count_claim_overlaps(claims):
    return np.sum(claims >= 2)


def main():

    testing = [
        '#1 @ 1,3: 4x4',
        '#2 @ 3,1: 4x4',
        '#3 @ 5,5: 2x2'
    ]

    text_array = get_input_text_array()

    claims = np.zeros((1000, 1000))

    add_claim_overlaps(text_array, claims)
    print(claims)

    print("{} square inches of fabric are within two or more claims".format(get_count_claim_overlaps(claims)))


if __name__ == '__main__':
    main()

'''
--- Part Two ---
Amidst the chaos, you notice that exactly one claim doesn't overlap by even a single square inch of fabric with any other claim. If you can somehow draw attention to it, maybe the Elves will be able to make Santa's suit after all!

For example, in the claims above, only claim 3 is intact after all claims are made.

What is the ID of the only claim that doesn't overlap?
'''