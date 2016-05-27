def solution(N):
    binary_form = "{0:b}".format(N)
    mylist = list(str(binary_form))
    one = 0
    count = 0;
    count_max = [0];
    length_list = len(mylist)
    c = 0
    for i in mylist:
        c = c + 1
        if i == '1':
            if one == 0:
                one = 1
            elif  one == 1:
                one = 0
                count_max = count_max.append(count)
                count = 0
        elif i == '0':
            count = count + 1
    maxi = max(count_max)
    return maxi
