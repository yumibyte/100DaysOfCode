def pyramid(n):
    counter = n
    list = []

    #while the val isn't nothing
    while counter != 0:

        #complete this for ea. layer
        for x in range(1, n + 1):
            print(x)
            nums = []
            #all the numbers in selected num
            for y in range(1, x + 1):

                nums.append(1)

            list.append(nums)
            counter -= 1
    return list
            
