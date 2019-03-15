#!/usr/bin/env python

import numpy as np

#penalty box
match    = 4
# mismatch handled by transitions & transversions
# ^more info: https://www.mun.ca/biology/scarr/Transitions_vs_Transversions.html 
gap      = -3
transitions = -2
transversions = -4

penalty_dict = {\
"A":{"A":match,"G":transitions,"C":transversions,"T":transversions},
"G":{"A":transitions,"G":match,"C":transversions,"T":transversions},
"C":{"A":transversions,"G":transversions,"C":match,"T":transitions},
"T":{"A":transversions,"G":transversions,"C":transitions,"T":match}}

#sequences. seq2 should always be larger than seq1
#original
seq1_1 = 'TGTTACGG'
seq2_1 = 'GGTTGACTA'

# additional sequences
seq1_2 = 'GACTTAC'
seq2_2 = 'CGTGAATTCAT'


def create_score_matrix(seq1, seq2):
    '''
    Create a matrix of scores representing trial alignments of the two sequences.
    Sequence alignment can be treated as a graph search problem. This function
    creates a graph (2D matrix) of scores, which are based on trial alignments
    of different base pairs. The path with the highest cummulative score is the
    best alignment.
    '''
    def calc_score(matrix, x, y):
        #Calculate score for a given x, y position in the scoring matrix.
        #The score is based on the up, left, and upper-left diagonal neighbors
        diag_score = matrix[x - 1][y - 1] + penalty_dict[seq1[x - 1]][seq2[y - 1]]
        up_score   = matrix[x - 1][y] + gap
        left_score = matrix[x][y - 1] + gap
        return max(0, diag_score, up_score, left_score)
    
    #scoring matrix size
    rows = len(seq1) + 1
    cols = len(seq2) + 1
    score_matrix = [[0 for col in range(cols)] for row in range(rows)]
    # Fill the scoring matrix.
    max_score = 0
    max_pos   = None    # The row and column of the highest score in matrix.
    for i in range(1, rows):
        for j in range(1, cols):
            score = calc_score(score_matrix, i, j)
            if score > max_score:
                max_score = score
                max_pos   = (i, j)
            score_matrix[i][j] = score
    assert max_pos is not None, 'the x, y position with the highest score was not found'
    return score_matrix, max_pos



def print_matrix(matrix,seq1,seq2):
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
def find_best_match_section(score_matrix,start_pos,seq1,seq2):
    cur = start_pos
    seq1_recon = ""
    seq2_recon = ""
    seq_matchings = ""
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
        if prior == 3:
            seq1_recon+=(seq1[row-1] if row > 0 else '-')
            seq2_recon+=(seq2[col-1] if col > 0 else '-')
            seq_matchings+=("*" if seq1[row-1] == seq2[col-1] else ".")
        elif prior == 2:
            seq1_recon+='-'
            seq2_recon+=(seq2[col-1] if col > 0 else '-')
            seq_matchings+=" "
        elif prior == 1:
            seq1_recon+=(seq1[row-1] if row > 0 else '-')
            seq2_recon+='-'
            seq_matchings+=" "
        cur = row+dir[0],col+dir[1]
        result.append(cur)
    res_str = (seq1_recon[::-1],seq2_recon[::-1],seq_matchings[::-1])
    return result,res_str
    
#end of your function(s)

if __name__ == '__main__':
    #my main
    print("original seq1='{}'\noriginal seq2='{}'".format(seq1_1,seq2_1))
    score_matrix, start_pos = create_score_matrix(seq1_1,seq2_1)
    print_matrix(score_matrix,seq1_1,seq2_1)
    path,res = find_best_match_section(score_matrix,start_pos,seq1_1,seq2_1)
    print('->'.join(map(lambda x:"({},{})".format(x[0],x[1]),path)))
    print("Match Results:\nseq1='{}'\nseq2='{}'\n     '{}'".format(*res))
    
    print("\noriginal seq1='{}'\noriginal seq2='{}'".format(seq1_2,seq2_2))
    score_matrix, start_pos = create_score_matrix(seq1_2,seq2_2)
    print_matrix(score_matrix,seq1_2,seq2_2)
    path,res = find_best_match_section(score_matrix,start_pos,seq1_2,seq2_2)
    print('->'.join(map(lambda x:"({},{})".format(x[0],x[1]),path)))
    print("Match Results:\nseq1='{}'\nseq2='{}'\n     '{}'".format(*res))
    