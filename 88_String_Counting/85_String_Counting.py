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

        if temp_combos[0] is None:
            pass
        elif len(temp_combos[0]) == 0:
            pass

        else:
            results = []
            first = temp_combos[0][0]
            remainder = temp_combos[1:]

            words = temp_combos[0]

            for word in words:
                for i in range(len(word)+1):
                    s = word[:i] + first + word[i:]
                    results.append(s)
            print(results)


#     for x in s:
#         position = alphabet.find(x)
#         while position != 25:
#             position += 1
#             total += 1
#             print(alphabet[position])


    return total
    
