import sys

def reducer():
    '''
    Given the output of the mapper for this exercise, the reducer should return one row
    per unit, along with the total number of ENTRIESn_hourly over the course of may. 
    
    You can assume that the input to the reducer is sorted by UNIT, such that all rows 
    corresponding to a particular UNIT are group together.

    '''
    

    register = {}
    for line in sys.stdin:
        data = line.split('\t')
        if len(data) != 2:
            continue
        unit, entries = data
        if unit in register:
            register[unit] += float(entries)
        else:
            register[unit] = float(entries)


    for key in register:
        msg = str(key) + '\t' + str(register[key])
        print msg

reducer()
