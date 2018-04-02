import re
import traceback
import random
import os
import time

def printGrid(Grid):
    print('=========')
    for i in range(9):
        for j in range(9):
            print(Grid[9*i+j]),
        print("")
    print('=========')
    
def isCorrect(grid,pos,val):
    grid[pos]=str(val)
    row = pos % 9
    t = grid[row:81:9]
    if(FindDuplicates(t)):
        #print 'row',
        return False

    cols = int(pos / 9)
    temp = grid[9 * cols:9 * cols + 9]
    if (FindDuplicates(temp)):
        #print 'cols',
        return False
    row = row / 3
    cols = cols / 3
    board = [[0,1,2,9,10,11,18,19,20],[3,4,5,12,13,14,21,22,23],[6,7,8,15,16,17,24,25,26],[27,28,29,36,37,38,45,46,47],[30,31,32,39,40,41,48,49,50],[33,34,35,42,43,44,51,52,53],[54,55,56,63,64,65,72,73,74],[57,58,59,66,67,68,75,76,77],[60,61,62,69,70,71,78,79,80]]
    temp = board[3*row + cols]
    t = []
    for i in range(9):
        t.append(grid[temp[i]])
    if (FindDuplicates(t)):
        #print 'grid',
        return False

    #print('OK')
    return True

def FindDuplicates(in_list):
    temp = []
    for x in in_list:
        if x not in temp or x == '.':
            temp.append(x)
    if(len(temp) == len(in_list)):
        return False
    return True

def hasSolution(Grid, t):
#    printGrid(Grid)
    num = 0
    while True:
        num += 1
        #print('try for',iterator[t],'value',num)
        if isCorrect(Grid,iterator[t],num) and num < 10:
            #print('fix for',iterator[t],'value',num)
            Grid[iterator[t]]=str(num);
            t+=1
            try:
                if not hasSolution(Grid, t):
                    Grid[iterator[t]]='.'
                    t-=1
                    #printGrid(Grid)
                    #print('reverting',iterator[t],'value','.')
                    continue
                else:
                    return True
            except:
                #print '>>> traceback <<<'
                #traceback.print_exc()

                #print '>>> end of traceback <<<'
                return True
        else:
            if num > 8:
                Grid[iterator[t]]='.'
                ##printGrid(Grid)
                #print("\nREVERSE")
                return False
def init(Grid):
    global iterator
    iterator = []
    global t
    t=0
    for i in range(81):
      if(Grid[i]=='.'):
          iterator.append(i)
      i+=1
    printGrid(Grid)
t=0
iterator = []
def main ():
  sampleGrid = ['.', '.', '3', '.', '2', '.', '6', '.', '.', '9', '.', '.', '3', '.', '5', '.', '.', '1', '.', '.', '1', '8', '.', '6', '4', '.', '.', '.', '.', '8', '1', '.', '2', '9', '.', '.', '7', '.', '.', '.', '.', '.', '.', '.', '8', '.', '.', '6', '7', '.', '8', '2', '.', '.', '.', '.', '2', '6', '.', '9', '5', '.', '.', '8', '.', '.', '2', '.', '3', '.', '.', '9', '.', '.', '5', '.', '1', '.', '3', '.', '.']
  # init(sampleGrid1)
  # if hasSolution (sampleGrid1,t):
  #   printGrid(sampleGrid2)
  # else: print 'NO SOLUTION for Grid1'

  begin = time.time()
  init(sampleGrid)
  if hasSolution (sampleGrid,t):
    printGrid(sampleGrid)
  else: print 'NO SOLUTION for Grid2'
  end = time.time()
  print("Time Taken: " + str(end-begin) + " sec")
if __name__ == "__main__":
    main()