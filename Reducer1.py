import sys
import string

last_patent = None
loc = "-"

for line in sys.stdin:
    line = line.strip()
    patent,location = line.split("\t")

    if not last_patent or last_patent != patent:
        last_patent = patent
        loc = location
    elif patent == last_patent:
        location = loc
        print '%s\t%s' % (patent,location)
