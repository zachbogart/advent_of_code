input = ""

with open("input.txt") as file:
    for line in file:
        input += line.strip()

# print(len(input))

# keep track of original length and jumping size
length_original = len(input)
next_num_jump = int(len(input) / 2)

# tack on the entire thing at the end for circular wrap
input = input + input

# go through the input and check if next is same as current
total = 0
for ind, num in enumerate(input):
    next_num = input[ind + next_num_jump]
    if next_num == num:
        total += int(num)

    if ind == (length_original - 1):
        break

print("Total: ", total)



'''
--- Part Two ---
You notice a progress bar that jumps to 50% completion. Apparently, the door isn't yet satisfied, but it did emit a star as encouragement. The instructions change:

Now, instead of considering the next digit, it wants you to consider the digit halfway around the circular list. That is, if your list contains 10 items, only include a digit in your sum if the digit 10/2 = 5 steps forward matches it. Fortunately, your list has an even number of elements.

For example:

1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
1221 produces 0, because every comparison is between a 1 and a 2.
123425 produces 4, because both 2s match each other, but no other digit has a match.
123123 produces 12.
12131415 produces 4.
What is the solution to your new captcha?

'''