def findMode(readList):
    numCount={}
    highestNum=0
    for i in readList:
        if i in numCount.keys(): numCount[i] += 1
        else: numCount[i] = 1
    for i in numCount.keys():
        if numCount[i] > highestNum:
            highestNum=numCount[i]
            mode=i
    if highestNum != 1: print(mode)
    elif highestNum == 1:
        #print("All elements of list appear once.")
        count = 1
        for key in sorted(numCount):
            if count == 1:
                # print "%s: %s" % (key, numCount[key])
                print "%s" % (key)
                count += 1
                exit(0)

    #print numCount
    #count = 1
    #for key in sorted(numCount):
    #    if count == 1:
    #        #print "%s: %s" % (key, numCount[key])
    #        print "%s" % (key)
    #        count += 1
    #        exit(0)

A = [4978, 11735, 14216, 14470, 38120, 51135, 64630, 67060, 73429, 99233]
findMode(A)