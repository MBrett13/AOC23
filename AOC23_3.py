def multiplyList(myList):
 
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result

with open('C:\\Users\mbrettle\OneDrive - Hitachi Solutions\Documents\AOC_input2.txt', 'r') as f:



    import statistics
    import re
    import numpy as np


    lines = f.readlines()
    commands = [line.strip() for line in lines]
    #two_d_array = [[char for char in row] for row in input_array]
    #commands = ["467..114..", "...*......", "..35..633.", "......#...", "617*......", ".....+.58.", "..592.....", "......755.", "...$.*....", ".664.598.."]
    #commands = ["12.......*..", "+.........34", ".......-12..", "..78........", "..*....60...", "78..........", ".......23...", "....90*12...", "............", "2.2......12.", ".*.........*", "1.1.......56"]
    #list = []
    bdict ={}
    otherlist = []
    nlist = []
    newlist = []
    inlist = []
    finlist = []
    y = 0
    for command in commands:
        pos = 0
        dnd = 0
        diglist = []
        poslist =[]
        tdict = {}
        i = commands.index(command)
        while pos < len(command):
            value = command[pos]
            if value.isdigit():
                diglist.append(value)
                poslist.append(pos)
                if dnd == 0:
                    dnd = 1
                #list.append([commands.index(command),pos])
            if (not value.isdigit() and dnd == 1) or (value.isdigit() and pos == len(command)-1):
                checklist = []
                dnd = 0
                check = 0
                odict = {}
                if poslist[0] == 0:
                    totlist = poslist + [poslist[-1] + 1]
                elif poslist[-1] == len(command)-1:
                    totlist = [poslist[0] -1] + poslist 
                else:
                    totlist = [poslist[0] -1] + poslist + [poslist[-1] + 1]
                for x in totlist:
                    if i != 0 and commands[i-1][x] == "*":
                        checklist.append(str(i-1) + "," + str(x))
                    if commands[i][x] == "*":
                        checklist.append(str(i) + "," + str(x))
                    if i != len(commands) - 1 and commands[i+1][x] == "*":
                        checklist.append(str(i+1)+"," + str(x))
                checklist = list(set(checklist))
                otherlist = otherlist + checklist
                for q in checklist:
                    nlist.append(''.join(diglist))
                #for o in odict:
                #    odict.update({o:''.join(diglist)})
                #if check == 1:
                    #list.append(int(''.join(diglist)))
                #for x in poslist:
                #    dict.update({x:''.join(diglist)})  
                #print(poslist)     
                diglist = []
                poslist = []
                #dict.update(odict)
            pos += 1

    for o in otherlist:
        if otherlist.count(o) > 1:
            inlist.append(o)
    inlist = list(set(inlist))

    arr1 = np.array(otherlist)
    arr2 = np.array(nlist)
    arr = np.stack((arr1, arr2), axis=1)

    filter_arr = []
    for element in arr:
        if element[0] in inlist:
            filter_arr.append(True)
        else:
            filter_arr.append(False) 
    arr = arr[filter_arr]

    for g in inlist:
        sumlist = []
        for element in arr:
            if element[0] == g:
                sumlist.append(int(element[1]))
        finlist.append(multiplyList(sumlist))
    print(sum(finlist))

