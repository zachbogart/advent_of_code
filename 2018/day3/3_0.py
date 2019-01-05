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
--- Day 3: No Matter How You Slice It ---
The Elves managed to locate the chimney-squeeze prototype fabric for Santa's suit (thanks to someone who helpfully wrote its box IDs on the wall of the warehouse in the middle of the night). Unfortunately, anomalies are still affecting them - nobody can even agree on how to cut the fabric.

The whole piece of fabric they're working on is a very large square - at least 1000 inches on each side.

Each Elf has made a claim about which area of fabric would be ideal for Santa's suit. All claims have an ID and consist of a single rectangle with edges parallel to the edges of the fabric. Each claim's rectangle is defined as follows:

The number of inches between the left edge of the fabric and the left edge of the rectangle.
The number of inches between the top edge of the fabric and the top edge of the rectangle.
The width of the rectangle in inches.
The height of the rectangle in inches.
A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3 inches from the left edge, 2 inches from the top edge, 5 inches wide, and 4 inches tall. Visually, it claims the square inches of fabric represented by # (and ignores the square inches of fabric represented by .) in the diagram below:

...........
...........
...#####...
...#####...
...#####...
...#####...
...........
...........
...........
The problem is that many of the claims overlap, causing two or more claims to cover part of the same areas. For example, consider the following claims:

#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
Visually, these claim the following areas:

........
...2222.
...2222.
.11XX22.
.11XX22.
.111133.
.111133.
........
The four square inches marked with X are claimed by both 1 and 2. (Claim 3, while adjacent to the others, does not overlap either of them.)

If the Elves all proceed with their own plans, none of them will have enough fabric. How many square inches of fabric are within two or more claims?
'''