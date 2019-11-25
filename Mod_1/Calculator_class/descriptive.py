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
        self.set_data()

    # Method that initalizes all attributes

    def set_data(self):
        self.length = len(self.data)
        self.mean = self._calc_mean()
        self.median = self._calc_median()
        self.variance = self._calc_variance()
        self.stand_dev = self._calc_std()

    # Method that adds new values to the data list

    def add_data(self, new_data):
        self.data.extend(new_data)
        self.set_data(self.data)

    # Method that searchs and removes values

    def remove_data(self, bad_data):
        self.data = [elem for elem in self.data if elem not in bad_data]
        self.set_data(self.data)

    def _calc_mean(self):
        return sum(self.data) / self.length

    # function that returns the median

    def _calc_median(self):

        # sort the data
        self.data = sorted(self.data)

        # Chech of odd number of values
        if len(self.data) % 2 != 0:
            return self.data[int(len(self.data) / 2)]

        # Do the even case
        return (self.data[(int(len(self.data) / 2)) - 1] +
                self.data[(int(len(self.data) / 2))]) / 2
    # variance fuction

    def _calc_variance(self):

        return (sum([(x - self._calc_mean(self.data))**2 for x in self.data])) / \
            (len(self.data) - 1)

    # standard deviation function

    def _calc_std(self):
        return (self._calc_variance(self.data))**.5
