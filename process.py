# This script implements regression

import os
import sys

filename = sys.argv[1]
if os.path.isfile(filename):
    output = os.popen('cat ' + filename)
    print output
else:
    print 'File does not exist!'
