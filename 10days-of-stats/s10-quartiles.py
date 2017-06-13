if __name__ == '__main__':
    n = int(raw_input().strip())
    if (n <= 4) or (n >= 51):
        print("error condition for n")
        exit(0)

    data = raw_input().strip().split(' ')

    for i in range(n):
        if int(data[i]) <= 0 or int(data[i]) > 100:
            print("error condition for Xi")

    median_q1 = 0
    median_q2 = 0
    median_q3 = 0
    data = [int(x) for x in data]
    data.sort()
    #print data
    data_length = len(data)
    #print "data_length is %s" % data_length
    if data_length % 2 == 0 and (data_length/2)%2 == 0:
        median_q1 = int(data[data_length / 2 / 2])
        median_q2 = (int(data[data_length/2]) + int(data[data_length/2 - 1])) / 2
        median_q3 = (int(data[(data_length / 2 + (data_length - 1)) / 2]) + int(data[((data_length / 2 + (data_length - 1)) / 2) +1])) / 2
        print median_q1
        print median_q2
        print median_q3
    elif data_length % 2 == 0 and (data_length/2)%2 == 1:
        median_q1 = int(data[data_length / 2 / 2])
        median_q2 = (int(data[data_length/2]) + int(data[data_length/2 - 1])) / 2
        median_q3 = int(data[(data_length / 2 + (data_length - 1)) / 2])
        print median_q1
        print median_q2
        print median_q3
    else:
        median_q1 = (int(data[data_length / 2 / 2]) + int(data[data_length / 2 / 2 - 1])) / 2
        median_q2 = int(data[(data_length-1)/2])
        median_q3 = (int(data[(data_length / 2 + (data_length - 1))/2] + int(data[(data_length / 2 + (data_length - 1))/2+1]))) / 2
        print median_q1
        print median_q2
        print median_q3