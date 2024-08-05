with open('C:\\Users\mbrettle\OneDrive - Hitachi Solutions\Documents\AOC_input7.txt', 'r') as f:



    import statistics
    import re
    import numpy as np
    import pandas as pd
    from statistics import mode

    
    handdict = {
     7:[5],
     6:[4,1],
     5:[3,2],
     4:[3,1,1],
     3:[2,2,1],
     2:[2,1,1,1],
     1:[1,1,1,1,1]
     }

    carddict = {
        "A":14, 
        "K":13, 
        "Q":12, 
        "J":0, 
        "T":10, 
        "9":9, 
        "8":8, 
        "7":7, 
        "6":6, 
        "5":5, 
        "4":4, 
        "3":3, 
        "2":2
    }


    lines = f.readlines()
    datas = [line.split()[0] for line in lines]
    hands = [[i for i in data] for data in datas]
    type_rank = []
    card_rank = []
    bids = [int(line.split()[1]) for line in lines]
    df = []
    #print(list(cards))
    #cards = np.array(cards)
    #arr = np.stack((cards,type_rank,card_rank))
    #print(type_rank.shape)
    #print(arr)
    for hand in hands:
        carddict["J"] = 0
        fhand = []
        thand = []
        for card in hand:
            fhand.append(carddict[card])
        
        if hand.count(0) == 5:
            carddict["J"] = 14
        elif mode(sorted(fhand,reverse = True)) == 0:
            carddict["J"] = max(fhand)
        else:
            carddict["J"] = mode(sorted(fhand,reverse = True))
        for card in hand:
            thand.append(int(carddict[card]))
        unique = list(dict.fromkeys(thand))
        typelist = []
        for card in unique:
            c = thand.count(card)
            typelist.append(c)
            typelist.sort(reverse = True)
        t =list(handdict.keys())[list(handdict.values()).index(typelist)]
        type_rank.append(t)
        carddict["J"] = 0
        for card in hand:
            hand[hand.index(card)] = int(carddict[card])
    hands = np.array(hands)
    #print(hands)
    type_rank = np.array(type_rank).reshape(len(type_rank),1)
    bids = np.array(bids).reshape(len(bids),1)
    arr = np.hstack((type_rank, hands, bids))
    print(arr)
    #print(type_rank.shape)
    #print(hands.shape)
    df = pd.DataFrame(arr)
    df.sort_values(by=[0,1,2,3,4,5,6], inplace=True)
    i=1
    tota = []
    print(df)
    for x in df.index:
        tot = i*int(df[6][x])
        tota.append(tot)
        i+=1
        
    print(tota)
    print(sum(tota))
 