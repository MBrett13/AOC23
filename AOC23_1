#Part 1

with open('/lakehouse/default/Files/AOC_Input.txt', 'r') as f:

    lines = f.readlines()
    commands = [line.strip() for line in lines]
    sumlist = []
    for command in commands:
        pos = 0
        diglist =[]
        i = commands.index(command)
        while pos < len(command):
            value = command[pos]
            if value.isdigit():
                diglist.append(value)
            pos += 1
        sumlist.append(int(diglist[0] + diglist[-1]))
    print(sum(sumlist))

#Part 2  

import re
with open('/lakehouse/default/Files/AOC_Input.txt', 'r') as f:
    values = {
        "one": "1", 
        "two": "2", 
        "three": "3", 
        "four": "4", 
        "five": "5", 
        "six": "6", 
        "seven": "7", 
        "eight": "8", 
        "nine": "9"
        }
    lines = f.readlines()
    commands = [line.strip() for line in lines]
    #commands = ["two1nine", "eightwothree","abcone2threexyz" , "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]
    sumlist = []
    for command in commands:
        pos = 0
        diglist =[]
        i = commands.index(command)
        while pos < len(command):
            value = command[pos]
            if value.isdigit():
                diglist.append(value)
            else:
                for x in values.keys():
                    if command[pos:].startswith(x):
                        diglist.append(values[x])
            pos += 1
        sumlist.append(int(diglist[0] + diglist[-1]))
    print(sum(sumlist))
