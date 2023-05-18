#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@File    :  test.py
@Time    :  :2023/05/16
@Author  :   Dr. Cat Lu / BFcat
@Version :   1.0
@Contact :   bfcat@live.cn
@Site    :   https://bg4xsd.github.io
@License :   (C)MIT License
@Desc    :   This is a part of project XXX, more details can be found on the site.
'''
'''
   为了调试代码，临时做的实验代码， 注意采用交互方式运行
'''
import os, sys
import numpy

def rk4(odes, state, parameters, dt=0.01):
    k1 = dt * odes(state, parameters)
    k2 = dt * odes(state + 0.5 * k1, parameters)
    k3 = dt * odes(state + 0.5 * k2, parameters)
    k4 = dt * odes(state + k3, parameters)
    return state + (k1 + 2 * k2 + 2 * k3 + k4) / 6

def generate(data_length, odes, state, parameters):
    data = numpy.zeros([state.shape[0], data_length])

    for i in range(5000):
        state = rk4(odes, state, parameters)

    for i in range(data_length):
        state = rk4(odes, state, parameters)
        data[:, i] = state

    return data

def lorenz_odes(a,b):
    x = a[0]
    y = a[1]
    z = a[2]
    sigma = b[0]
    beta = b[1]
    rho = b[2]
    return numpy.array([sigma * (y - x), x * (rho - z) - y, x * y - beta * z])


def lorenz_generate(data_length):
    return generate(data_length, lorenz_odes, \
        numpy.array([-8.0, 8.0, 27.0]), numpy.array([10.0, 8/3.0, 28.0]))

data = lorenz_generate(2**13)

