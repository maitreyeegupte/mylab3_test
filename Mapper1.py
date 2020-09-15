import sys

for line in sys.stdin:
    patent = ""
    location = "-"
    cite = "-"

    line = line.strip()
    splits = line.split(",")
    if len(splits) == 2:
        patent = splits[0]
    else:
        patent = splits[0]
        location = splits[5]
    print '%s\t%s\t%s' % (patent,location)
        
