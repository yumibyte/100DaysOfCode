def solve(s):

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#     s = list(s)
    print(s)

    position = 0
    total = 0
    combinations = []
#loop through each letter
    for i in range(0, len(s)):
        print(i)
        temp_combos = []

        # split letters into all combos
        left = s[0:i]
        right = s[i:]

        temp_combos = [left]
        temp_combos.extend([right])

        print(temp_combos)

        # roll through all letters
        for x in temp_combos:
            print(x)
#             position = alphabet.find(x)
#             while position != 25:
#                 position += 1



#     for x in s:
#         position = alphabet.find(x)
#         while position != 25:
#             position += 1
#             total += 1
#             print(alphabet[position])


    return total
