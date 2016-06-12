import sys
import string

"""from util import mapper_logfile
logging.basicConfig(filename=mapper_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')"""

def mapper():
    """
    The input to this mapper will be the final Subway-MTA dataset.  This mapper 
    should return a line for each UNIT, along with the number of ENTRIESn_hourly for that row.
    
    An example input to the mapper may would look like this:
    R002    1050105.0
    
    The mapper should emit a key and value pair separated by a tab, for example:
    R002\t105105.0
    """

    keys = []

    for line in sys.stdin:
        data = line.split(',')
        if data[0] == "":
            keys = data
        else:
            data_point = dict(zip(keys,data))
            print str(data_point['UNIT']) + '\t' + str(data_point['ENTRIESn_hourly'])
                                    

mapper()