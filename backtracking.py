#citations

#https://www.programiz.com/python-programming/methods/built-in/ord
#https://medium.com/algorithms-and-leetcode/backtracking-e001561b9f28
#https://www.tutorialspoint.com/python_data_structure/python_backtracking.htm
#https://www.tutorialspoint.com/python_data_structure/python_hash_table.htm


import sys
import time
from itertools import *

#This program takes words as input, for each unique letter in each word it is replaced by a nubmber until the first and second word summed,equals the last word.If an particular assignment cannot lead to a solve, backtrack and reassign.

ht={}
def backtrack(words):
        if (len(words[2])>len(words[1])):
               isCarry=True
        letters = list(set(''.join(words)))
        for permutation in permutations(range(10), len(letters)):
            number=1
            lookuplist = dict(zip(letters, permutation)) #create lookuplist
            #check all permutations until first+second = third
            if all(lookuplist[w[0]] > 0 for w in words): 
                #print(lookuplist)
                numbers = [convert(w, lookuplist) for w in words]
                #print(ht)
                for num in ht.values():
                    if num == numbers:
                        numbers=[convert(w,lookuplist) for w in words]
                        ht[number]=numbers
                        if isCarry:
                            if ht[number][2][0]<1:
                                numbers=[convert(w,lookuplist) for w in words]
                                ht[number]=numbers
                    if ((ht[number][0]+ht[number][1])==ht[number][2]):
                        print("solved!:",numbers)
                    else:
                        number=number+1




def convert(word, lookup):
    return int(''.join(str(lookup[letter]) for letter in word))

if __name__ == '__main__':
    st=time.time() #start timer
    print("Backtracking Solve")
    if (len(sys.argv) < 4 or len(sys.argv) > 4):
        print('Must have three inputs')
    else:
        words=sys.argv[1:] #take input from the users and store in list
        print("Solving ...:",words)
        backtrack(words)

            # get the end time
        et = time.time()	
            # get the execution time
        elapsed_time = et - st
        print('Execution time:', elapsed_time, 'seconds')
