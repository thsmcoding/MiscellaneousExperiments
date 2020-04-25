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


def makeexchanges(j, gui):
    myrectangles = gui.rectangles
    gui.canvas.itemconfig(myrectangles[j], fill=COLORS[12])
    gui.listBars[j].setColor(COLORS[12])
    ti.sleep(0.2)
    if gui.listBars[j].data < gui.listBars[j-1].data:
        gui.swapNumber(j,j-1) 
        ti.sleep(0.2)
        gui.setColor(j-1, 0)
    gui.setColor(j, 0)
    ti.sleep(0.3)    
    
def makeexchangesimproved(j,i, gui):
    myrectangles = gui.rectangles
    gui.canvas.itemconfig(myrectangles[j], fill=COLORS[12])
    gui.listBars[j].setColor(COLORS[12])
    ti.sleep(0.8)
    if gui.listBars[i].data < gui.listBars[j-1].data:
        gui.swapNumber(j,j-1) 
        ti.sleep(0.2)
        gui.setColor(j-1, 0)
    ti.sleep(0.3)  
    if  j == 0:
        print("DO YOUR ZERO")
        gui.swapNumber(i,j)
    gui.setColor(j, 0)
    gui.setColor(i, 0)   
    
    
    
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
    ti.sleep(0.5)
    gui.setColor(current, 0)
    gui.setColor(_min, 0)
    
    

def insertionAlgorithm(current,gui):
    print("Starting insertion algorithm")
    myrectangles = gui.rectangles
    bars = gui.listBars    
    ti.sleep(0.4)
    gui.canvas.itemconfig(myrectangles[current], fill=COLORS[11])
    gui.listBars[current].setColor(COLORS[11])
    ti.sleep(0.2)
    l = [makeexchanges(j,gui) for j in range(current,0, -1)] 
    gui.setColor(current, 0)


def bubbleAlgorithm(current, gui):
    N = gui.numbers
    l = [makeexchanges(j, gui) for j in range(1, N-current, 1)] 
    

def insertionAlgorithmImproved(current, gui):
    print("Insertion Algorithm - version improved")
    myrectangles = gui.rectangles
    bars = gui.listBars    
    gui.canvas.itemconfig(myrectangles[current], fill=COLORS[11])
    gui.listBars[current].setColor(COLORS[11])
    ti.sleep(0.4)
    l = [makeexchangesimproved(j,current, gui) for j in range(current,-1, -1)] 
    gui.setColor(current, 0)  
    
    




def mergesortAlgorithm(listBars,gui):
    print("Starting mergeSort algorithm")


def quicksortAlgorithm(listBars,gui):
    print("Starting quicksort algorithm")


def priorityQueueAlgorithm(listBars,gui):
    print("Starting selection algorithm")


switcherFunction = {"Selection" : selectionAlgorithm,
                    "Insertion" : insertionAlgorithm,
                    "Insertionimproved":insertionAlgorithmImproved,
                    "Bubble" : bubbleAlgorithm,
                    "Mergesort" : mergesortAlgorithm,
                    "Quicksort": quicksortAlgorithm,
                    "Priority Queue": priorityQueueAlgorithm}
