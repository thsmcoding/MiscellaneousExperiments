# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 07:45:20 2020
@author:HTS
"""

import time as ti
import random as rd
from Start.setup_mod import COLORS


def generateRandomArray(n, _min, _max):
    l = []
    size = int(n)
    print("Starting generating random numbers")
    for i in range(0, size):
        r = rd.randint(_min, _max)
        l.append(r)
    return l

def findPotentialMinimum(i, gui):
    bars = gui.listBars
    _min = i
    for u in range(i+1,len(bars)):
        if  bars[u].data < bars[_min].data:
            _min = u
    return _min
    
    
def selectionAlgorithm(current,gui):
    myrectangles = gui.rectangles
    gui.canvas.itemconfig(myrectangles[current], fill=COLORS[11])
    gui.listBars[current].setColor(COLORS[11])
    ti.sleep(0.2)
    _min = findPotentialMinimum(current,gui)
    if ( _min != current):
            gui.canvas.itemconfig(myrectangles[_min], fill=COLORS[12])
            gui.listBars[_min].setColor(COLORS[12])
            ti.sleep(0.4)
            gui.swapNumber(current, _min)        
    ti.sleep(0.6)
    gui.setColor(current, 0)
    gui.setColor(_min, 0)
    
    

def insertionAlgorithm(listBars,gui):
    print("Starting insertion algorithm")



def bubbleAlgorithm(listBars,gui):
    print("Starting bubble algorithm")



def mergesortAlgorithm(listBars,gui):
    print("Starting mergeSort algorithm")


def quicksortAlgorithm(listBars,gui):
    print("Starting quicksort algorithm")


def priorityQueueAlgorithm(listBars,gui):
    print("Starting selection algorithm")


switcherFunction = {"Selection" : selectionAlgorithm,
                    "Insertion" : insertionAlgorithm,
                    "Bubble" : bubbleAlgorithm,
                    "Mergesort" : mergesortAlgorithm,
                    "Quicksort": quicksortAlgorithm,
                    "Priority Queue": priorityQueueAlgorithm}
