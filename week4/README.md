# I have filled out the missing code for the smith-waterman aligner in python

Sequence is hardcoded in script.

'.out' files contain the dynamic programming table used and the coordinates used to climb back

I have tweaked the source code a bit to make it nicer.

contents of alignment of 'TGTTACGG' vs 'GGTTGACTA':
```
       0   1   2   3   4   5   6   7   8   9  
     | -   G   G   T   T   G   A   C   T   A  
  -------------------------------------------
0  - | 0   0   0   0   0   0   0   0   0   0  
1  T | 0   0   0   3   3   1   0   0   3   1  
2  G | 0   3   3   1   1   6   4   2   1   0  
3  T | 0   1   1   6   4   4   3   1   5   3  
4  T | 0   0   0   4   9   7   5   3   4   2  
5  A | 0   0   0   2   7   6   10  8   6   7  
6  C | 0   0   0   0   5   4   8   13  11  9  
7  G | 0   3   3   1   3   8   6   11  10  8  
8  G | 0   3   6   4   2   6   5   9   8   7  
(6,7)->(5,6)->(4,5)->(4,4)->(3,3)->(2,2)->(2,1)->(1,0)
```

contents of alignment of 'GACTTAC' vs 'CGTGAATTCAT':
```
       0   1   2   3   4   5   6   7   8   9   10  11 
     | -   C   G   T   G   A   A   T   T   C   A   T  
  ---------------------------------------------------
0  - | 0   0   0   0   0   0   0   0   0   0   0   0  
1  G | 0   0   3   1   3   1   0   0   0   0   0   0  
2  A | 0   0   1   0   1   6   4   2   0   0   3   1  
3  C | 0   3   1   0   0   4   3   1   0   3   1   0  
4  T | 0   1   0   4   2   2   1   6   4   2   0   4  
5  T | 0   0   0   3   1   0   0   4   9   7   5   3  
6  A | 0   0   0   1   0   4   3   2   7   6   10  8  
7  C | 0   3   1   0   0   2   1   0   5   10  8   7  
(6,10)->(5,9)->(5,8)->(4,7)->(3,6)->(2,5)->(1,4)->(1,3)->(1,2)->(0,1)
```