

if __name__ == '__main__':
    N = int(raw_input().strip())
    if (N <= 9) or (N >= 2501):
        print("error condition for N")
        exit(0)

    data = raw_input().strip().split(' ')

    sum = 0
    for i in range(N):
        if int(data[i]) <= 0 or int(data[i]) > 100000:
            print("error condition for Xi")
        sum += int(data[i])
    mean = sum/float(N)

    print "%.1f" % mean


    median = 0
    data = [int(x) for x in data]
    data.sort()
    #print data
    data_length = len(data)
    if data_length % 2 == 0:
        median = (int(data[data_length/2]) + int(data[data_length/2 - 1])) / float(2)
        print median
    else:
        median = int(data[data_length]) / float(2)
        print median

    mode_dict = {}
    highestNum = 0
    for i in data:
        if i in mode_dict.keys():
            mode_dict[i] += 1
        else:
            mode_dict[i] = 1
    for i in mode_dict.keys():
        if mode_dict[i] > highestNum:
            highestNum = mode_dict[i]
            mode = i

    for key in sorted(mode_dict):
        if mode_dict[key] == highestNum:
            print "%s" % key
            exit(0)

'''
    #print "highestNum is %s" % highestNum
    #if highestNum != 1:
    #    print(mode)
    if highestNum == 1:
    #elif highestNum == 1:
        # print("All elements of list appear once.")
        #count = 1
        for key in sorted(mode_dict):
            if mode_dict[key] == 1:
                # print "%s: %s" % (key, numCount[key])
                print "%s" % (key)
                #count += 1
                exit(0)
    elif highestNum == 2:
        #print("All highest elements of list appear twice.")
        #count = 2
        for key in sorted(mode_dict):
            #print "%s: %s" % (key, mode_dict[key])
            if mode_dict[key] == 2:
                #print "%s: %s" % (key, mode_dict[key])
                print "%s" % (key)
                #count += 1
                exit(0)

    #print sorted(mode_dict)
'''