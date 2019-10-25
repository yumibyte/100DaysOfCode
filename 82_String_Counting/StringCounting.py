def solve(s):

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    s = list(s)

    print(s)

    position = 0
    total = 0
#loop through each letter
    for x in s:
        position = alphabet.find(x)
        while position != 25:
            position += 1
            total += 1
            print(alphabet[position])


    return total
    
