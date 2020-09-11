import sys

for line in sys.stdin:
    patent = ""
    location = "-"
    cite = "-"

    line = line.strip()
    splits = line.split("/t")
    if len(splits) == 2:
        patent = splits[0]
    else:
        patent = splits[0]
        location = splits[x]
    print '%s\t%s\t%s' % (patent,location)
        
