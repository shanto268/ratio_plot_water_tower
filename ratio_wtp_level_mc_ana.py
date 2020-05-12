#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 20:21:20 2020
@author: sshanto

"""
import csv
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit 
from scipy import stats
import numpy as np
import scipy as sp


inputFiles = ["wt01ft.txt","wt09ft.txt", "wt11ft.txt","wt13ft.txt", "wt15ft.txt", "wt18ft.txt", "wt20ft.txt", "wt32ft.txt","wt50ft.txt"]
#inputFiles = ["wt13ft.txt", "wt15ft.txt", "wt18ft.txt", "wt20ft.txt", "wt32ft.txt","wt50ft.txt"]
heights = []
minZvalues = []


def readFile(fname):
        with open(fname,'r') as csvfile:
            vals = csv.reader(csvfile, delimiter=',')
            ratio = []
            wtp_height = int(fname[2:4])
            for row in vals:
                if row[0] != "nan":
                    ratio.append(float(row[0]))
            getMinRatioVal(wtp_height, ratio)

def getMinRatioVal(level, ratio):
    heights.append(level)
    ratio.sort()
    if ratio.pop(0) == 0.0:
        ratio.pop(0)        
    minZvalues.append(min(ratio))
          

def getStatsFit(x,y):
    z = np.polyfit(x, y, 2)
    f = np.poly1d(z)
    print(len(x))
    print(len(z))
    # calculate new x's and y's
    x_new = np.linspace(x[0], x[-1], 50, endpoint=True)
    y_new = f(x_new)
    plt.plot(x,y,'o', x_new, y_new)
    plt.xlabel("Height of Water (ft)")
    plt.ylabel("Ratio (wtp / away) ")
    plt.title("Ratio data vs height of water")
    plt.legend()
    plt.show()

def getStatsQuad(x,y):
    params = curve_fit(quadFunc, x, y)
    [a, b, c] = params[0]
    yval = []
    for i in x:
        yval.append(a*(i**2) + b*(i) + c)
    plt.plot(x, y, 'o', label='original data')
    plt.plot(x, yval, 'r', label='%f x^2 + %f x + %f'% (a, b, c))
    plt.xlabel("Height of Water (ft)")
    plt.ylabel("Ratio (wtp / away) ")
    plt.title("Ratio data vs height of water")
    plt.legend()
    plt.show()
    print('The equation is %f x^2 + %f x + %f'% (a, b, c))
    
def quadFunc(x, a, b, c):
    return a*(x**2) + b*(x) + c

def getStatsLinear(x,y):
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    print("slope: %f    intercept: %f" % (slope, intercept))
    print("R-squared: %f" % r_value**2)
    yval = []
    for i in range(len(x)):
        yval.append(intercept + slope*x[i])
    plt.plot(x, y, 'o', label='original data')
    plt.plot(x, yval, 'r--', label='%f x + %f'% (slope, intercept))
    plt.xlabel("Height of Water (ft)")
    plt.ylabel("Ratio (wtp / away) ")
    plt.title("Ratio data vs height of water")
    plt.legend()
    plt.show()
    
def createPlot():
    plt.scatter(heights, minZvalues)
    plt.xlabel("Height of Water (ft)")
    plt.ylabel("Ratio (wtp / away) ")
    plt.title("Ratio data vs height of water")
    plt.show()

def getStatsExponential(x,y):
        popt, pcov = curve_fit(exp_func, x, y)
        [a, b, c] = popt
        yval = []
        for i in x:
                yval.append(a*np.exp(-b*i) + c)
        plt.plot(x, y, 'o', label='original data')
        plt.plot(x, yval, 'r', label='%f e^{-%f x} + %f'% (a, b, c))
        plt.xlabel("Height of Water (ft)")
        plt.ylabel("Ratio (wtp / away) ")
        plt.title("Ratio data vs height of water")
        plt.legend()
        plt.show()

def getFit(x,y):
# Non-linear Fit
    A, K, C = fit_exp_nonlinear(x, y)
    fit_y = model_func(x, A, K, C)
    plt.plot(x, fit_y, 'b-', label='Fitted Function:\n $y = %0.2f e^{%0.2f t} + %0.2f$' % (A, K, C))
    plt.plot(x, y, 'o', label='original data')
    plt.xlabel("Height of Water (ft)")
    plt.ylabel("Ratio (wtp / away) ")
    plt.title("Ratio data vs height of water")
    plt.legend()
    plt.show()


def model_func(t, A, K, C):
    return A * np.exp(-K * np.asarray(t)) + C

def fit_exp_nonlinear(t, y):
    opt_parms, parm_cov = sp.optimize.curve_fit(model_func, t, y, maxfev=1000)
    A, K, C = opt_parms
    return A, K, C

def createReport():
    for i in inputFiles: 
        readFile(i)
    createPlot() 
 #   getStatsQuad(heights, minZvalues)
    getStatsLinear(heights, minZvalues)
 #   getStatsExponential(heights, minZvalues)
#    getFit(heights, minZvalues,1)
 #   getFit(heights, minZvalues)
   
#main function
createReport()
    
    
