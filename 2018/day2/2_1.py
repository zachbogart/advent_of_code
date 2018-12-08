def get_input_text_array():

    input = []
    # history = {}
    # total = 0
    # round = 1

    with open("input.txt") as file:
        for line in file:
            input.append(line[:-1])

    return input

def get_correct_IDs(input_array):
    for item1 in input_array:
        for item2 in input_array:
            if item1 != item2:
                faults = 0
                for ind in range(len(item1)):
                    if item1[ind] != item2[ind]:
                        faults += 1
                    if faults > 1:
                        break
                if faults == 1:
                    print("Found something: {}, {}".format(item1, item2))
                    return item1, item2

    print("Nothing happened...")

def get_common_letters(item1, item2):
    result = ''
    for letter_ind in range(len(item1)):
        if item1[letter_ind] == item2[letter_ind]:
            result += item1[letter_ind]
    return result


testing = [
    'abcde',
    'fghij',
    'klmno',
    'pqrst',
    'fguij',
    'axcye',
    'wvxyz'
]

text_array = get_input_text_array()
correct_id_1, correct_id_2 = get_correct_IDs(text_array)
print("Letters common between two correct IDs: {}".format(get_common_letters(correct_id_1, correct_id_2)))




'''
--- Part Two ---
Confident that your list of box IDs is complete, you're ready to find the boxes full of prototype fabric.

The boxes will have IDs which differ by exactly one character at the same position in both strings. For example, given the following box IDs:

abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
The IDs abcde and axcye are close, but they differ by two characters (the second and fourth). However, the IDs fghij and fguij differ by exactly one character, the third (h and u). Those must be the correct boxes.

What letters are common between the two correct box IDs? (In the example above, this is found by removing the differing character from either ID, producing fgij.)
'''