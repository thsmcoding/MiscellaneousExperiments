# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 07:45:20 2020
@author:HTS
"""

import time as ti
import random as rd
from Start.setup_mod import COLORS
import copy as cp


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
    
    
def merge(gui, low, mid, high):
    rect_copies = [ cp.deepcopy(r) for r in gui.rectangles]
    bars_copies = [ cp.deepcopy(b) for b in gui.listBars]
    aux_rect = [r for r in rect_copies]
    aux_bars = [b for b in bars_copies]
    indexes = [low, mid+1]
    for k in range(low, high+1):
        temp_k = gui.listBars[k]
        gui.deleteRectangle(k)
        if indexes[0] > mid:
            temp = aux_bars[indexes[1]]
            gui.listBars[k].setAttributes(temp_k.x1, temp.y1, temp_k.x2, temp.y2, temp.data)
            gui.rectangles[k] = gui.createRectanglefrombar(gui.listBars[k], color=temp.getColor,i=k)
            indexes[1] +=1
        elif indexes[1] > high:
            temp = aux_bars[indexes[0]]
            gui.listBars[k].setAttributes(temp_k.x1, temp.y1, temp_k.x2, temp.y2, temp.data)
            gui.rectangles[k] = gui.createRectanglefrombar(gui.listBars[k], color=temp.getColor(),i=k)
            indexes[0] +=1
        elif aux_bars[indexes[0]].data < aux_bars[indexes[1]].data:
            temp = aux_bars[indexes[0]]
            gui.listBars[k].setAttributes(temp_k.x1, temp.y1, temp_k.x2, temp.y2, temp.data)
            gui.rectangles[k] = gui.createRectanglefrombar(gui.listBars[k], color=temp.getColor(),i=k)
            indexes[0] +=1   
        else:
            temp = aux_bars[indexes[1]]
            gui.listBars[k].setAttributes(temp_k.x1, temp.y1, temp_k.x2, temp.y2, temp.data)
            gui.rectangles[k] =gui.createRectanglefrombar(gui.listBars[k], color=temp.getColor(),i=k) 
            indexes[1] +=1

    
def mergesortTDAlgorithm(gui, low, high):
    if low >= high:
        return    
    mid = low + (high-low)//2
    gui.canvas.itemconfig(gui.rectangles[mid], fill=COLORS[11])
    ti.sleep(0.2)
    gui.canvas.itemconfig(gui.rectangles[mid], fill=COLORS[0])
    ti.sleep(0.4)
    aux_rect = []
    aux_bars = []
    mergesortTDAlgorithm(gui, low, mid)
    mergesortTDAlgorithm(gui, mid+1, high)    
    merge(gui, low,mid,high)


def mergesortBUAlgorithm(gui, low, high):
    print("Starting mergesortBUAlgorithm algorithm")
    N = high+1
    size =1
    while size < N:
        i = 0
        while i < N-size:
            gui.canvas.itemconfig(gui.rectangles[i+size-1], fill=COLORS[11])
            ti.sleep(0.1)
            gui.canvas.itemconfig(gui.rectangles[i+size-1], fill=COLORS[0])
            merge(gui,i,i+size-1, min(i+size+size-1, N-1))
            i += size+size
        size = size+size
        

def quicksortPartition(gui, low, high):
    myrectangles = gui.rectangles
    _indexList = [low+1, high]
    if low >= high:
        return -1    
    check_validity = True
    while check_validity == True:
        while gui.listBars[_indexList[0]].data <= gui.listBars[low].data :
            if _indexList[0] == high:
                break
            _indexList[0] +=1            
        while gui.listBars[_indexList[1]].data > gui.listBars[low].data:
            if _indexList[1] == low:
                break
            _indexList[1] -=1      
        if _indexList[0] >=_indexList[1]:
            check_validity = False
        else:
            gui.swapNumber(_indexList[0],_indexList[1])        
    gui.swapNumber(low, _indexList[1])
    gui.canvas.itemconfig(myrectangles[low], fill=COLORS[0])    
    gui.canvas.itemconfig(myrectangles[high], fill=COLORS[0])
    return _indexList[1]
                   
    
    
def quicksort3wayAlgorithm(gui, low, high):
    if high <= low:
        return None    
    current = gui.listBars[low].data
    _indexList = [low, low+1, high]    
    while _indexList[1] <= _indexList[2]:
        gui.canvas.itemconfig(gui.rectangles[_indexList[1]], fill=COLORS[11])
        gui.canvas.itemconfig(gui.rectangles[_indexList[1]], fill=COLORS[0])         
        if  gui.listBars[_indexList[1]].data < current:
            gui.swapNumber(_indexList[1], _indexList[0])
            _indexList[0] +=1
            _indexList[1] +=1     
            ti.sleep(0.4)        
        elif gui.listBars[_indexList[1]].data > current:
            gui.swapNumber(_indexList[1], _indexList[2])
            _indexList[2] -=1            
        else:
            _indexList[1] +=1
    quicksort3wayAlgorithm(gui,low, _indexList[0]-1)
    quicksort3wayAlgorithm(gui, _indexList[2]+1, high)
        
    
     
def quicksortAlgorithm(gui, low, high):
    print("Starting quicksort algorithm")
    if low >= high:
        return None
    myrectangles = gui.rectangles
    gui.canvas.itemconfig(myrectangles[low], fill=COLORS[11])    
    gui.canvas.itemconfig(myrectangles[high], fill=COLORS[11])
    ti.sleep(0.1)
    j_found = quicksortPartition(gui, low, high)
    if (j_found != -1):
        gui.canvas.itemconfig(myrectangles[j_found], fill=COLORS[14])
    ti.sleep(0.5)   
    # gui.canvas.itemconfig(myrectangles[low], fill=COLORS[0])    
    # gui.canvas.itemconfig(myrectangles[high], fill=COLORS[0])
    if (j_found != -1):
        gui.canvas.itemconfig(myrectangles[j_found], fill=COLORS[0])
    ti.sleep(0.3)      
    quicksortAlgorithm(gui, low, j_found-1)
    quicksortAlgorithm(gui, j_found+1, high)
    

def priorityQueueAlgorithm(listBars,gui):
    print("Starting selection algorithm")




switcherFunction = {"Selection" : selectionAlgorithm,
                    "Insertion" : insertionAlgorithm,
                    "Insertionimproved":insertionAlgorithmImproved,
                    "Bubble" : bubbleAlgorithm,
                    "Quicksort": quicksortAlgorithm,
                    "Quick3waySort":quicksort3wayAlgorithm,
                    "Priority Queue": priorityQueueAlgorithm,
                    "MergesortBU" : mergesortBUAlgorithm,
                     "MergesortTD": mergesortTDAlgorithm
                    }
