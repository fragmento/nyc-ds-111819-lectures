# Functions


import math

# function that returns the mean


def calc_mean(data):
    return sum(data)/len(data)

# function that returns the median


def calc_median(data):

    # sort the data
    sorted(data)

    # Chech of odd number of values
    if len(data) % 2 != 0:
        return data[int(len(data)/2)]

    # Do the even case
    return (data[(int(len(data)/2))-1]+data[(int(len(data)/2))])/2

# variance fuction


def calc_var(data):

    return (sum([(x-calc_mean(data))**2 for x in data]))/(len(data)-1)

# standard deviation function


def calc_std(data):
    return (calc_var(data))**.5

# write formula to calculate covariance


def calc_cov(data1, data2):
    a = [(v-calc_mean(data2)) for v in data2]
    b = [(x-calc_mean(data1)) for x in data1]
    return sum([a[i]*b[i] for i in range(len(data1))])/(len(data1)-1)

# write formula to calculate correlation


def calc_corr(data1, data2):
    return calc_cov(data1, data2)/(calc_std(data1)*calc_std(data2))
