with open('C:\\Users\mbrettle\OneDrive - Hitachi Solutions\Documents\AOC_input8.txt', 'r') as f:



    import statistics
    import re
    import numpy as np
    import pandas as pd
    from statistics import mode

    lines = f.readlines()
    alls = [line.strip() for line in lines]
    instructs = [all for all in alls[0]]
    thisdict = {}
    for i in alls[2:]:
        a = re.split(r"[\W]+", i)
        thisdict.update({a[0] : a[1:3]})
    d = "AAA"
    c = 0
    while d != "ZZZ":
        for instruct in instructs:
                print(instruct)
                node = thisdict[d]
                if instruct == "L":
                    d = node[0]
                else:
                    d = node[1]
                c += 1
                print(d)
    print(c)