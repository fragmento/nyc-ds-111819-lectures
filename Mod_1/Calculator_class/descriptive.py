#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:25:52 2019
@author: swilson5
"""
import math


class Calculator:

    def __init__(self, data):
        self.data = data
        self.set_data(self.data)

    # Method that initalizes all attributes

    def set_data(self, data):
        self.length = len(data)
        self.mean = self._calc_mean(data)
        self.median = self._calc_median(data)
        self.variance = self._calc_variance(data)
        self.stand_dev = self._calc_std(data)

    # Method that adds new values to the data list

    def add_data(self, new_data):
        self.data.extend(new_data)
        self.set_data(self.data)

    # Method that searchs and removes values

    def remove_data(self, bad_data):
        self.data = [elem for elem in self.data if elem not in bad_data]
        self.set_data(self.data)

    def _calc_mean(self, data):
        return sum(data) / len(data)

    # function that returns the median

    def _calc_median(self, data):

        # sort the data
        data = sorted(data)

        # Chech of odd number of values
        if len(data) % 2 != 0:
            return data[int(len(data) / 2)]

        # Do the even case
        return (data[(int(len(data) / 2)) - 1] +
                data[(int(len(data) / 2))]) / 2

    # variance fuction

    def _calc_variance(self, data):

        return (sum([(x - self._calc_mean(data))**2 for x in data])) / \
            (len(data) - 1)

    # standard deviation function

    def _calc_std(self, data):
        return (self._calc_variance(data))**.5


data = [2, 20, 45, 15, 10, 55, 80]
instance = Calculator(data)
instance.remove_data([80])
print(instance.data)
