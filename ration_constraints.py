#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: Shanto

"""
import csv
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit 
from scipy import stats
import numpy as np

inputFiles = ["wt00ft.txt", "wt05ft.txt","wt07ft.txt","wt09ft.txt", "wt11ft.txt","wt13ft.txt", "wt15ft.txt", "wt18ft.txt", "wt20ft.txt", "wt32ft.txt","wt50ft.txt"]

height = []
min_ratio = []

constraint = 18

#the following code extracts and constraints the space for the ratio
def readFile(fname):
    with open(fname,'r') as csvfile:
        xval = []
        yval = []
        ratio = []
        vals = csv.reader(csvfile, delimiter=';')
        wtp_height = int(fname[2:4])
        for line in vals:
            x = float(line[0])
            y = float(line[1])
            if x >= -constraint and x <= constraint:
                if y >= -constraint and y <= constraint:
                    rat = float(line[2])
                    ratio.append(rat)
                    xval.append(x)
                    yval.append(y)
        print("Minimum value for height "+ str(wtp_height) + " : " + str(min(ratio)))    
        height.append(wtp_height)
        min_ratio.append(min(ratio))

def createPlots(x,y):
    plt.scatter(x, y)
    plt.xlabel("Height of Water (ft)" )
    plt.ylabel("Ratio (wtp / away) ")
    plt.title("Ratio data vs height of water [ -" + str(constraint) + ", "  + str(constraint) + " ]")
    plt.ylim(0,1)
    plt.savefig("ratio_constraint"+str(constraint)+".png")
    plt.show()

def createReport():
    for i in inputFiles: 
        readFile(i)
    createPlots(height,min_ratio)
    
createReport()
