if __name__ == '__main__':
    N = int(raw_input().strip())
    if (N <= 4) or (N >= 51):
        print("error condition for N")
        exit(0)

    data = raw_input().strip().split(' ')
    weight_data = raw_input().strip().split(' ')

    sum = 0
    weight_sum = 0
    for i in range(N):
        if int(data[i]) <= 0 or int(data[i]) > 100000 or int(weight_data[i]) <= 0 or int(weight_data[i]) > 100:
            print("error condition for Xi/Wi")
        sum += int(data[i]) * int(weight_data[i])
        weight_sum += int(weight_data[i])
    weighted_mean = sum/float(weight_sum)

    print "%.1f" % weighted_mean
    