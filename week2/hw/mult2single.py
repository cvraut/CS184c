# read in multiline fasta through stdin
# output single line fasta to stdout

import sys
begin = True

for line in sys.stdin:
    line = line.strip()
    if line.startswith('>'):
        if not begin:
            print()
        print(line)
    else:
        print(line,end="")
    begin = False
    