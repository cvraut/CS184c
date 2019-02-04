#!/usr/bin/env python

import numpy as np

#penalty box
match    = 3
mismatch = -3
gap      = -2

penalty_dict = {\
"A":{"A":3,"G":-3,"C":-3,"T":-3},
"G":{"A":-3,"G":3,"C":-3,"T":-3},
"C":{"A":-3,"G":-3,"C":3,"T":-3},
"T":{"A":-3,"G":-3,"C":-3,"T":3}}

#sequences. seq2 should always be larger than seq1
#original
seq1 = 'TGTTACGG'
seq2 = 'GGTTGACTA'

# additional sequences
seq1 = 'GACTTAC'
seq2 = 'CGTGAATTCAT'

#scoring matrix size
rows = len(seq1) + 1
cols = len(seq2) + 1

def create_score_matrix(rows, cols):
    '''
    Create a matrix of scores representing trial alignments of the two sequences.
    Sequence alignment can be treated as a graph search problem. This function
    creates a graph (2D matrix) of scores, which are based on trial alignments
    of different base pairs. The path with the highest cummulative score is the
    best alignment.
    '''
    score_matrix = [[0 for col in range(cols)] for row in range(rows)]
    # Fill the scoring matrix.
    max_score = 0
    max_pos   = None    # The row and columbn of the highest score in matrix.
    for i in range(1, rows):
        for j in range(1, cols):
            score = calc_score(score_matrix, i, j)
            if score > max_score:
                max_score = score
                max_pos   = (i, j)
            score_matrix[i][j] = score
    assert max_pos is not None, 'the x, y position with the highest score was not found'
    return score_matrix, max_pos

def calc_score(matrix, x, y):
    #Calculate score for a given x, y position in the scoring matrix.
    #The score is based on the up, left, and upper-left diagnol neighbors
    diag_score = matrix[x - 1][y - 1] + penalty_dict[seq1[x - 1]][seq2[y - 1]]
    up_score   = matrix[x - 1][y] + gap
    left_score = matrix[x][y - 1] + gap
    return max(0, diag_score, up_score, left_score)

def print_matrix(matrix):
    '''
    Print the scoring matrix.
    ex:
    0   0   0   0   0   0
    0   2   1   2   1   2
    0   1   1   1   1   1
    0   0   3   2   3   2
    0   2   2   5   4   5
    0   1   4   4   7   6
    '''
    #print(np.matrix(matrix))
    form = lambda x: "{:3s}".format(str(x))
    print("      ", " ".join(map(form,range(len(seq2)+1))))
    print("     |"," ".join(map(form,'-'+seq2)))
    print(" ","-"*(3+4*(len(seq2)+1)))
    for i in range(len(matrix)):
        print(form(i)+("-"+seq1)[i],end=' | ')
        print(" ".join(map(form,matrix[i])))

#add your function(s) to find a solution here.
def find_best_match_section(score_matrix,start_pos):
    cur = start_pos
    
    result = [cur]
    while score_matrix[cur[0]][cur[1]] != 0:
        row,col = cur
        #print("({},{})->".format(row,col),end="")
        diag = score_matrix[row-1][col-1] if row > 0 and col > 0 else -1
        diag = (diag,3,(-1,-1))
        top = score_matrix[row][col-1] if col > 0 else -1
        top = (top,2,(0,-1))
        left = score_matrix[row-1][col] if row > 0 else -1
        left = (left,1,(-1,0))
        win,prior,dir = max(diag,top,left)
        cur = row+dir[0],col+dir[1]
        result.append(cur)
        
    return result
    
#end of your function(s)

if __name__ == '__main__':
    #my main
    score_matrix, start_pos = create_score_matrix(rows, cols)
    print_matrix(score_matrix)
    print('->'.join(map(lambda x:"({},{})".format(x[0],x[1]),find_best_match_section( score_matrix,start_pos))))