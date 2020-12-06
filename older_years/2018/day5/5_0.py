import time

def get_input_text_string():

    input = ''

    with open("input.txt") as file:
        for line in file:
            input += line[:]

    return input



def main():
    start = time.time()

    text_string = get_input_text_string()

    # text_string = "dabAcCaCBAcCcaDA"

    print(len(text_string))

    while True:
        a_thing_happened = False

        for char_ind in range(0, len(text_string) - 1):

            next_char = text_string[char_ind + 1]
            lowercase_version = chr(ord(text_string[char_ind]) + 32)
            uppercase_version = chr(ord(text_string[char_ind]) - 32)
            foo = 0

            if next_char == lowercase_version and text_string[char_ind].isupper():
                foo = len(text_string)
                # print(text_string[char_ind] + next_char)
                text_string = text_string[:char_ind] + text_string[char_ind + 2:]
                a_thing_happened = True
                # print(foo - len(text_string))
                break

            if next_char == uppercase_version and text_string[char_ind].islower():
                foo = len(text_string)
                # print(text_string[char_ind] + next_char)
                text_string = text_string[:char_ind] + text_string[char_ind + 2:]
                a_thing_happened = True
                # print(foo - len(text_string))
                break

        if not a_thing_happened:
            break

    print(text_string)
    print("Resulting polymer contains {} units".format(len(text_string)))

    end = time.time()
    print(end - start)


if __name__ == '__main__':
    main()

'''
--- Day 5: Alchemical Reduction ---
You've managed to sneak in to the prototype suit manufacturing lab. The Elves are making decent progress, but are still struggling with the suit's size reduction capabilities.

While the very latest in 1518 alchemical technology might have solved their problem eventually, you can do better. You scan the chemical composition of the suit's material and discover that it is formed by extremely long polymers (one of which is available as your puzzle input).

The polymer is formed by smaller units which, when triggered, react with each other such that two adjacent units of the same type and opposite polarity are destroyed. Units' types are represented by letters; units' polarity is represented by capitalization. For instance, r and R are units with the same type but opposite polarity, whereas r and s are entirely different types and do not react.

For example:

In aA, a and A react, leaving nothing behind.
In abBA, bB destroys itself, leaving aA. As above, this then destroys itself, leaving nothing.
In abAB, no two adjacent units are of the same type, and so nothing happens.
In aabAAB, even though aa and AA are of the same type, their polarities match, and so nothing happens.
Now, consider a larger example, dabAcCaCBAcCcaDA:

dabAcCaCBAcCcaDA  The first 'cC' is removed.
dabAaCBAcCcaDA    This creates 'Aa', which is removed.
dabCBAcCcaDA      Either 'cC' or 'Cc' are removed (the result is the same).
dabCBAcaDA        No further actions can be taken.
After all possible reactions, the resulting polymer contains 10 units.

How many units remain after fully reacting the polymer you scanned? (Note: in this puzzle and others, the input is large; if you copy/paste your input, make sure you get the whole thing.)
'''