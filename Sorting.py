# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 23:35:11 2017

@author: ma
"""
def BubbleSort(arr):
    n = len(arr)
    for i in range(0,n):
        for j in range(i,n):
            if arr[j]<arr[i]:               
                arr[i], arr[j] = arr[j], arr[i]


def BubbleSortRecc(arr):
    n = len(arr)
    for i in range(0,n-1):
        j = i+1
        if arr[j]<arr[i]:               
            arr[i], arr[j] = arr[j], arr[i]
            BubbleSort(arr)
                

def insertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        for j in range(0,i):
            if(arr[i]<arr[j]):
                arr[i], arr[j] = arr[j], arr[i]

def insertionSortRec(arr):
    n = len(arr)
    for i in range(1,n):
            if(arr[i]<arr[i-1]):
                arr[i], arr[i-1] = arr[i-1], arr[i]
                insertionSortRec(arr)
                
def selectionSort(arr):
    n = len(arr)    
    minIndex= 0
    for j in range(0,n):
        min = arr[j]
        for i in range(j,n):
            if(min>arr[i]):
                min = arr[i]
                minIndex = i
        arr[j],arr[minIndex] = arr[minIndex],arr[j]
        

def mergeSort(arr):
   
    if len(arr)>1:
        midpoint = len(arr)//2
        leftArray = arr[:midpoint]
        rightArray = arr[midpoint:]
        mergeSort(leftArray)
        mergeSort(rightArray)
        leftIndex = 0
        rightIndex = 0
        tempIndex = 0
        
        while leftIndex<len(leftArray) and rightIndex<len(rightArray):
            if leftArray[leftIndex]<rightArray[rightIndex]:
                arr[tempIndex] = leftArray[leftIndex]
                leftIndex +=1
                tempIndex +=1
            else:
                arr[tempIndex] = rightArray[rightIndex]
                rightIndex +=1
                tempIndex +=1
                
        while leftIndex<len(leftArray):
            arr[tempIndex] = leftArray[leftIndex]
            leftIndex +=1
            tempIndex +=1
                
        while rightIndex<len(rightArray):
            arr[tempIndex] = rightArray[rightIndex]
            rightIndex +=1
            tempIndex +=1
                

def quickSort(arr):
    leftArray = []
    rightArray = []
   
    if len(arr)>1:
        pvPoint = arr[0]
        for i in range(1,len(arr)):
            if arr[i] < pvPoint:
                leftArray.append(arr[i])
            else:
                rightArray.append(arr[i])

        arr = leftArray
        arr.append(pvPoint)
        arr.append(rightArray)
       
        quickSort(arr[len(leftArray):])
        quickSort(arr[:len(leftArray)+1])
      
                      
            
def countingSort(arr):
    n = len(arr)
    indexArr = [0 for i in range(0,11)]
    countArr = [0 for i in range(0,n)]
    print(indexArr)   
    print(countArr)   

    for i in range(0,n):
        val = arr[i]
        print(val)
        indexArr[val] +=1  

    for i in range(0,n):
       indexArr[i] +=indexArr[i-1]   

        
    for j in arr:
        
        sortedindex = indexArr[j]
        countArr[sortedindex] = j
        indexArr[j]-= 1
       
    print(countArr)

                    
    
                   
        
        
                
    
arr = [9,8,5,10,1,5,4,3,3]
countingSort(arr)
            
    
