with open('C:\\Users\mbrettle\OneDrive - Hitachi Solutions\Documents\AOC_input5test.txt', 'r') as f:



    import statistics
    import re
    #import numpy as np


    data = f.read()
    splats = data.split("\n\n")
    seeds =[]
    maps =[]
    lines = [splat.split("\n") for splat in splats]
    seeds = [line.split() for line in lines[0]][0][1:]
    mappings = [[i.split() for i in line[1:]] for line in lines[1:]]
    seed_pairs = [(int(seeds[i]), int(seeds[i]) + int(seeds[i + 1])) for i in range(0, len(seeds), 2)]
    print(seed_pairs)
    #maps = [[[*map(int, n.split())] for n in i.split("\n")[1:]] for i in data.split("\n\n")[1:]]
    print(mappings)
    #lines = [splat.split("\n") for splat in splats]
    #print(maps)
    locations = []
    for x in seeds:
        for m in mappings:
            for map in m:
              if int(map[1]) <= int(x) < (int(map[1]) + int(map[2])):
                  idx = int(x) - int(map[1])
                  x = int(map[0]) + idx
                  break
        locations.append(x)
    closest = min(locations)
    print(closest)

    #splats = ["seed-to-soil map:\n50 98 2\n52 50 48\n"]
    sdict = {}
    lines = []
    seeds =[]
    slist = []
    llist = []
    sstart = []
    dstart = []
    send = []
    lines = [splat.split("\n") for splat in splats]
    i = 1
    mappings = [line[0] for line in lines[1:]]
    bdict = dict.fromkeys(line[0] for line in lines[1:])
    #print(bdict)
    for line in lines[1:]:
        #del line[0]
        commands = line[1:]
        sarr = []
        darr = []
        for command in commands:
            maps = command.split()
            #print(maps)
            sstart.append(int(maps[1]))
            send.append(int(maps[1]) + int(maps[2]))
            dstart.append(int(maps[0]))
        arr = np.array(zip(sstart,send,dstart))
        bdict.update({line[0]:arr})
    print(bdict)
    seeds = [line.split() for line in lines[0]][0][1:]
    j=0
    #print(seeds)
    for seed in seeds:
        seed = int(seed)
        if seed in bdict[mappings[0]].keys():
            soil = bdict[mappings[0]][seed]
        else:
            soil = seed
        #print(soil)
        if soil in bdict[mappings[1]].keys():
            fert = bdict[mappings[1]][soil]
        else:
            fert = soil
        #print(fert)
        if fert in bdict[mappings[2]].keys():
            wate = bdict[mappings[2]][fert]
        else:
            wate = fert
        #print(wate)
        if wate in bdict[mappings[3]].keys():
            ligh = bdict[mappings[3]][wate]
        else:
            ligh = wate
        #print(ligh)
        if ligh in bdict[mappings[4]].keys():
            temp = bdict[mappings[4]][ligh]
        else:
            temp = ligh
        #print(temp)
        if temp in bdict[mappings[5]].keys():
            humi = bdict[mappings[5]][temp]
        else:
            humi = temp
        #print(humi)
        if humi in bdict[mappings[6]].keys():
            loca = bdict[mappings[6]][humi]
        else:
            loca = humi
        #print(loca)
        slist.append(seed)
        llist.append(loca)
    closest = min(llist)
    #llist.index(closest)

        
    print(closest)
    print(bdict[mappings[6]])

         

    maps = [command.strip() for command in commands]
    print(maps)
    for command in commands:
            print(command[7])
    for map in maps:
            i = 0
            while i < map[2]:
                seedsoil.update({map[1]:map[2]})
                i += 1
    print(seedsoil)
            #dstart = map[0]
            #dend = map[0] + map[2]
            #sstart = map[1]
            #send = map[1] + map [2]





    print(len(splat))
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

