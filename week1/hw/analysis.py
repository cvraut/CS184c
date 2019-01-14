# intended for python 3.6+

from random import random
from bisect import bisect_right
from functools import reduce
from collections import defaultdict
import re
import numpy as np

# file to use as obs data (NOTE: must be fasta format)
fasta_filename = "Zmay_chr_9-P-94283818.fa"
#fasta_filename = "ant_genome.fna"

# assume uniform prob for each of the 4 nucleotides
prob_n = {"A":0.25,"C":0.25,"T":0.25,"G":0.25}
assert(sum(prob_n.values())==1.0)

nucleotides = list(prob_n.keys())
n_thresh = np.cumsum([prob_n[n] for n in nucleotides])

k_mers = [set(prob_n.keys())]
for i in range(2,11):
    k_mers.append(set())

# include nucleotide sequences I'm curious about
k_mers[1].add("TA")# tata box
k_mers[1].add("AA")
k_mers[2].add("ATG")# codon for start
    
    
    
for i in range(2,11):
    while len(k_mers[i-1]) < 5:
        i_mer=""
        for k in range(i):
            i_mer+=nucleotides[bisect_right(n_thresh,random())]
        k_mers[i-1].add(i_mer)
    
print("Using '{}' as observational fasta data".format(fasta_filename))

# check for occurrence of overlapping matches
total_checks = defaultdict(int)
total_hits = defaultdict(int)

# functionality for multi-line fasta
fasta = []
for line in open(fasta_filename):
    if not line.startswith(">"):
        fasta[-1]+=line.upper().strip()
    else:
        fasta.append("")

print("lines to get through: {}\n".format(len(fasta)))    

line_cnt = 1
for line in fasta:
    if not line.startswith(">"):
        for si in range(len(line)):
            for i_mers in k_mers:
                for i_mer in i_mers:
                    if si+len(i_mer) > len(line):
                        break
                    elif line[si:si+len(i_mer)] == i_mer:
                        total_hits[i_mer]+=1
                    total_checks[i_mer]+=1
        # check if the find alg worked using regex -> it does
        """
        for i_mers in k_mers:
            for i_mer in i_mers:
                print(i_mer,total_hits[i_mer],total_checks[i_mer])
                assert(total_hits[i_mer]==len(re.findall("(?={})".format(i_mer),line)))# check if hits is correct
                assert(total_checks[i_mer]==(len(line)-len(i_mer)+1))# check if checks is correct
        """
        # really only helps when size of data is in MB, makes sure program hasn't halted
        if line_cnt%int(1000*random()+1) == 0:
            print("finished line #{}".format(line_cnt))
        line_cnt+=1

#'''
print("    K-mer    |  Theo. P(occurrence)  |  Obs. P(occurrence)")
for i in range(1,11):
    print("----------------------------------------------------------")
    print("Random {:2d}-mers ({} checks):".format(i,total_checks[list(k_mers[i-1])[0]]))
    print("----------------------------------------------------------")
    for k_mer in k_mers[i-1]:
        prob = reduce((lambda x,y:x*y),[prob_n[n] for n in k_mer])
        print(" {:11s} |   {:15.13f}     |   {:15.13f}".format(k_mer,prob,total_hits[k_mer]/total_checks[k_mer]))
#'''