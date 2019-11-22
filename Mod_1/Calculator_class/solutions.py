#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:25:52 2019

@author: swilson5
"""
import math


class Calculator:

    def __init__(self, data):
        self.data = sorted(data)
        self._calc_stats()

    def _calc_mean(self):
        return self.total/self.length

    def _calc_median(self):
        n = self.length
        if n % 2 == 1:
            return self.data[(n-1)//2]
        else:
            return (self.data[n//2-1]+self.data[n//2])/2

    def _calc_variance(self):
        sum_value = 0
        for item in self.data:
            sum_value += (item - (self.mean))**2
        return sum_value/(self.length-1)

    def _calc_stddev(self):
        return math.sqrt(self.variance)

    def _calc_stats(self):
        self.length = len(self.data)
        self.total = sum(self.data)
        self.mean = self._calc_mean()
        self.median = self._calc_median()
        self.variance = self._calc_variance()
        self.stand_dev = self._calc_stddev()

    def add_data(self, new_data):
        """Takes a list of data, adds all of those values
            from the data set of the object,
            and recalculates the descriptive statistics.
        """
        self.data.extend(new_data)
        self.data = sorted(self.data)
        self._calc_stats()
        return

    def remove_data(self, new_data):
        """Takes a list of data, removes all of those values
            from the data set of the object,
            and recalculates the descriptive statistics.
        """
        self.data = [x for x in self.data if x not in new_data]
        self._calc_stats()
        return

    
