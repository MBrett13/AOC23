with open('C:\\Users\mbrettle\OneDrive - Hitachi Solutions\Documents\AOC_input4.txt', 'r') as f:



    import statistics
    import re
    import numpy as np


    lines = f.readlines()
    commands = [line.strip() for line in lines]
    #two_d_array = [[char for char in row] for row in input_array]
    #commands = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53", "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19", "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1", "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83", "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36", "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]
    #commands = ["12.......*..", "+.........34", ".......-12..", "..78........", "..*....60...", "78..........", ".......23...", "....90*12...", "............", "2.2......12.", ".*.........*", "1.1.......56"]
    list = []
    tot = []
    odict = {}
    for r in range(1,len(commands)+1):
        odict.update({r:int(1)})
    i = 1
    for command in commands:
        x = command.split(":")[1]
        y = x.split("|")
        winning = y[0].split()
        mine = y[1].split()
        tot = [m for m in mine if m in winning]
        agg = len(tot)
        o = 0
        while o < odict[i]:
            j=1
            for t in tot:
                odict.update({i+j : odict[i+j]+1})
                j += 1
            o += 1
        i += 1
    k = 1
    for command in commands:
        list.append(odict[k])
        k += 1
    print(sum(list))

