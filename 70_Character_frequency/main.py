# return a list of tuples sorted by frequency with
# the most frequent letter first. Any letters with the
# same frequency are ordered alphabetically
import string
def letter_frequency(text):
  # TODO get and sort letter frequency of text
    text = text.replace(" ", "")

    puncuation = "\'\"?/\!@#$%^&*()[]{}<>-_=+"

    for x in text:
        if x in puncuation:
            print(x)
            text.replace(x, " ")
    print(text)

    tuples = {}
    for letter in text.lower():
#         print(x)
        if letter in tuples:
            tuples[letter] += 1
        else:
            tuples[letter] = 1

#     print(tuples)
    return tuples
