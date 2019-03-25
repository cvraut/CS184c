# This is some code to do some Smith-Waterman alignment on 2 gene sequences.
# Now with support to handle matching differences between transitions and transversions
# And support to print the matched subsections of the sequences

Sequence, match, gap, transitions, and transversions values are hardcoded in script.

Match is set to:        +4
Gap is set to:          -3
Transition is set to:   -2
Transversion is set to: -4 

I chose these values as I wanted integer values for all the penalties, and I wanted to 
support the claim that transversions are twice as unlikely as transitions and gap 
penalties fall somewhere in between.

'.out' file contains the dynamic programming table and output of the python script.

```
original seq1='TGTTACGG'
original seq2='GGTTGACTA'
seq1 match portion ='G-TTA-C'
seq2 match portion ='GGTTGAC'
                    '* **. *'

original seq1='GACTTAC'
original seq2='CGTGAATTCAT'
seq1 match portion ='G--ACTT-A'
seq2 match portion ='GTGAATTCA'
                    '*  *.** *'
```

'*' - match
'.' - mismatch
' ' - gap
