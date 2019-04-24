import random
import time
import statistics
import numpy as np

# Main function to call the other five in one call
def main():

    n = 10000
    def random_array (n):
        array = []
        for i in range (0, n, 1):
            array.append(random.randint(0, 100))
        return array  

# Bubble Sort
# Code taken from http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html
    def bubbleSort(alist):                       
        for passnum in range(len(alist)-1,0,-1):  
            for i in range(passnum):              
                if alist[i]>alist[i+1]:           
                    temp = alist[i]               
                    alist[i] = alist[i+1]         
                    alist[i+1] = temp

 # number of times the function will be run                   
    num_runs = 10
 # an array to store the test results   
    results = []


# Code snippet provided on project specification to log times
    for r in range (num_runs):

        start_time = time.time()               
        alist = (random_array(n))
        bubbleSort(alist)
     #  print(alist)
        end_time = time.time()
        time_elapsed = end_time - start_time

        results.append(time_elapsed)
     # print (time_elapsed)

    np.mean(time_elapsed)
    print (time_elapsed)
    

# Merge Sort
# code taken from http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html
    def mergeSort(alist):
    
        if len(alist)>1:
            mid = len(alist)//2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]

            mergeSort(lefthalf)
            mergeSort(righthalf)

            i=0
            j=0
            k=0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    alist[k]=lefthalf[i]
                    i=i+1
                else:
                    alist[k]=righthalf[j]
                    j=j+1
                k=k+1

            while i < len(lefthalf):
                alist[k]=lefthalf[i]
                i=i+1
                k=k+1

            while j < len(righthalf):
                alist[k]=righthalf[j]
                j=j+1
                k=k+1
# number of times the function will be run  
    num_runs = 10
 # an array to store the test results 
    results = []

# Code snippet provided on project specification to log times
    for r in range (num_runs):

        start_time = time.time()                
        alist = (random_array(n))
        mergeSort(alist)
      # print(alist)
        end_time = time.time()
        time_elapsed = end_time - start_time

        results.append(time_elapsed)
      # print (time_elapsed)

    np.mean(time_elapsed)
    print (time_elapsed)
     

# Insertion Sort
# code taken from http://interactivepython.org/runestone/static/pythonds/SortSearch/TheInsertionSort.html
    def insertionSort(alist):
        for index in range(1,len(alist)):

            currentvalue = alist[index]
            position = index

            while position>0 and alist[position-1]>currentvalue:
                alist[position]=alist[position-1]
                position = position-1

        alist[position]=currentvalue

# number of times the function will be run  
    num_runs = 10
# an array to store the test results 
    results = []


# Code snippet provided on project specification to log times
    for r in range (num_runs):

        start_time = time.time()               
        alist = (random_array(n))
        insertionSort(alist)
      # print(alist)
        end_time = time.time()
        time_elapsed = end_time - start_time

        results.append(time_elapsed)
      # print (time_elapsed)

    np.mean(time_elapsed)
    print (time_elapsed)
     

# Selection Sort
# code taken from http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html
    def selectionSort(alist):
            for fillslot in range(len(alist)-1,0,-1):
                positionOfMax=0
            for location in range(1,fillslot+1):
                if alist[location]>alist[positionOfMax]:
                    positionOfMax = location

                temp = alist[fillslot]
                alist[fillslot] = alist[positionOfMax]
                alist[positionOfMax] = temp
# number of times the function will be run  
    num_runs = 10
# an array to store the test results     
    results = []

# Code snippet provided on project specification to log times
    for r in range (num_runs):

        start_time = time.time()               
        alist = (random_array(n))
        selectionSort(alist)
      # print(alist)
        end_time = time.time()
        time_elapsed = end_time - start_time

        results.append(time_elapsed)
      # print (time_elapsed)

    np.mean(time_elapsed)
    print (time_elapsed)


# Counting Sort
# Code taken from https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-10.php
    def counting_sort(alist, max_val):
        m = max_val + 1
        count = [0] * m                
        
        for a in alist:
        # count occurences
            count[a] += 1             
        i = 0
        for a in range(m):            
            for c in range(count[a]):  
                alist[i] = a
                i += 1
        return alist

# number of times the function will be run  
    num_runs = 10
# an array to store the test results     
    results = []

# Code snippet provided on project specification to log times
    for r in range (num_runs):

        start_time = time.time()               
        alist = (random_array(n))
        max_val = (10000)
        counting_sort(alist, max_val)
      # print(alist)
        end_time = time.time()
        time_elapsed = end_time - start_time
        
        results.append(time_elapsed)
      # print (time_elapsed)   

    np.mean(time_elapsed)
    print (time_elapsed)



if __name__ == "__main__": main()