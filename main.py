


#citations
#https://www.geeksforgeeks.org/permutation-and-combination-in-python/
#https://developers.google.com/optimization/cp/cryptarithmetic
#https://www.datacamp.com/tutorial/sets-in-python
#https://www.w3schools.com/python/python_dictionaries.asp
#https://realpython.com/python-zip-function/
#https://github.com/mgstabrani/cryptarithmetic #brute solver program

import sys
import time
from itertools import *

#This program takes words as input, for each unique letter in each word it is replaced by a nubmber until the first and second word summed,equals the last word.


def convert(word, lookup):
    return int(''.join(str(lookup[letter]) for letter in word))

if __name__ == '__main__':
    st=time.time() #start timer
    print("Brute Force Solve")
    if (len(sys.argv) < 4 or len(sys.argv) > 4):
        print('Must have three inputs')
    else:
        words=sys.argv[1:] #take input from the users and store in list
        print("Solving ...:",words)
        letters = list(set(''.join(words)))
        for permutation in permutations(range(10), len(letters)):
            lookuplist = dict(zip(letters, permutation)) #create lookuplist
            #check all permutations until first+second = third
            if all(lookuplist[w[0]] > 0 for w in words): 
                #print(lookuplist)
                numbers = [convert(w, lookuplist) for w in words]
            if ((numbers[0]+numbers[1]) == numbers[2]):
                print("solved!:",numbers)
            # get the end time
        et = time.time()	
            # get the execution time
        elapsed_time = et - st
        print('Execution time:', elapsed_time, 'seconds')
