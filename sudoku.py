import random

def SudokuGenerate():
    success = False
    i=0
    while success == False:
        i+=1
        grid = []
        grid.append([0,0,0,0,0,0,0,0,0])
        grid.append([0,0,0,0,0,0,0,0,0])
        grid.append([0,0,0,0,0,0,0,0,0])
        grid.append([0,0,0,0,0,0,0,0,0])
        grid.append([0,0,0,0,0,0,0,0,0])
        grid.append([0,0,0,0,0,0,0,0,0])
        grid.append([0,0,0,0,0,0,0,0,0])
        grid.append([0,0,0,0,0,0,0,0,0])
        grid.append([0,0,0,0,0,0,0,0,0])    
        for row in range(len(grid)):
            #initializing after ever row
            rowavail = [1,2,3,4,5,6,7,8,9]
            sum = 3
            RBTR = grid[row-1][-3:]
            availdict = {}
            for col in range(len(grid)):
                colavail = [1,2,3,4,5,6,7,8,9]
                rowabove = grid[row-1]
                Avail = rowavail[:]
                #print()
                #print(row,col)
                #print()
                #print('Avail   ',Avail)
                #print('row     ',rowavail)
                #print('collumn ',colavail)
                #print('rowabove',rowabove)
                #print('RBTR    ',RBTR)             
                #print()
                
                #collumn start
                #print('collumn ',colavail)
                #print('Avail   ',Avail)
                for chkrow in range(len(grid)):
                    if grid[chkrow][col] in colavail:
                        colavail.remove(grid[chkrow][col])
                #print('*collumn',colavail)
                
                #comparing lists and editing final availablilities
                Avail = [item1 for item1 in Avail if item1 in colavail]
                        
                #print('*Avail ',Avail)
                #print()
                #collumn ^
                
                
                #box start
                #print('rowabove',rowabove)
                #print('Avail   ',Avail)
                
                #rows 1 4 7 only need collumn restrictions, i think ???
                notbox = []           
                #rows 2 5 8
                if row%3==1:
                    #col 1 2 3
                    if col//3==0:
                        rowabove=rowabove[3:]
                        #print("*owabove",rowabove)
                    #col 4 5 6
                    elif col//3==1:
                        rowabove=rowabove[:3]+rowabove[6:]
                        #print("*owabove",rowabove)
                    #col 7 8 9
                    else:
                        rowabove=rowabove[:6]
                        #print("*owabove",rowabove)
                    
                    #comparing lists and editing final availablilities
                    Avail = [item2 for item2 in Avail if item2 in rowabove]
                    notbox = [item5 for item5 in range(10) if item5 not in rowabove]
                    
                    #print('*Avail ',Avail)
                    #print()
                    
                    
                #rows 3 6 9
                elif row%3==2:
                    #col 1 2 3
                    if col//3==0:
                        sameboxrows = grid[row-1][:3]+grid[row-2][:3]
                        #print("*samebox",sameboxrows)
                    #col 4 5 6
                    elif col//3==1:
                        sameboxrows = grid[row-1][3:6]+grid[row-2][3:6]
                        #print("*samebox",sameboxrows)
                    #col 7 8 9
                    if col//3==2:
                        sameboxrows = grid[row-1][6:]+grid[row-2][6:]
                        #print("*samebox",sameboxrows)
                    
                    #comparing lists and editing final availablilities
                    Avail = [item3 for item3 in Avail if item3 not in sameboxrows]
                    notbox = sameboxrows[:]
                    
                    #print('*Avail ',Avail)
                    #print()
                #box ^
                
                #print('notbox',notbox)
                #print()
                
                #print("RBTR    ",RBTR)
                #print ("*collumn",colavail)
                RBTR2 = [item4 for item4 in RBTR if item4 in colavail]
                #print("*RBTR   ",RBTR2)
                #print()
                
                
                
                if sum == col and col//3==1 and row%3==1:
                    if len(RBTR2)>0:
                        dig = random.choice(RBTR2)
                    else:
                        dig = 0
                elif len(Avail)>0:
                    dig = random.choice(Avail)
                else:
                    dig = 0
                #print("dig",dig)
                #print()
                #print("sum",sum)
                
                #print("avail before swap",Avail)
                if dig !=0:
                    Avail.remove(dig)
                    #print("avail after removing dig",Avail)
                
                availdict[dig] = [[row,col],Avail]
                #print ('***collumn dict',availdict)            
                
                replace = False
                if dig == 0:
                    #print ('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
                    for key, value in availdict.items():
                        for num in rowavail[:]:
                            #print('')
                            #print('if ((num in value[1]) & (key in colavail) & (key not in notbox)):')
                            #print(num,value[1],key,colavail,key,notbox)
                            if ((num in value[1]) & (key in colavail) & (key not in notbox)):
                                #print (key,'-',value)
                                for rownum in value[1]:
                                    #print('loop rownum',rownum)
                                    if rownum in rowavail:
                                        #print('rownum in rowavail',rownum)
                                        #print('[value[0][0]][value[0][1]]',value[0][0],value[0][1])
                                        grid[value[0][0]][value[0][1]] = rownum
                                        dig = key
                                        #print('dig = key')
                                        #print(dig,key)
                                        dig2 = rownum
                                        #print('dig2 = rownum')
                                        #print(dig2,rownum)
                                        replace = True
                                        break
                            if replace == True:
                                break
                        if replace == True:
                            break
                
                grid[row][col]=dig
                
                if replace == True:
                    dig = dig2
                if dig != 0:
                    rowavail.remove(dig)            
                
    
                
                if dig in RBTR:
                    sum += 1
                    RBTR.remove(dig)
                
                #print()
                #print('AVAIL   ',Avail)
                #print('ROW     ',rowavail)
                #print('COLLUMN ',colavail)
                #print()
                
                
        for row2 in grid:
            print (row2)
        print('try:',i)
        print()
        success = False
        for row3 in grid:
            if 0 in row3:
                success = False
                #print('success',success)
                break
            else:
                success = True
                #print('success',success)
    return (grid)

#def SudokuErase():
#    return()

#def SudokuSolve():
#    return()

SudokuGenerate()

#SudokuErase()

#SudokuSolve()
