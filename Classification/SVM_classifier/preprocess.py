import sys

__author__ = 'oleksandr'

if len(sys.argv) != 3:
    print 'wrong parameters...'
    exit()

data_path = sys.argv[1]
output_path = sys.argv[2]




# generating output
f = open(output_path, 'w')

f.close()