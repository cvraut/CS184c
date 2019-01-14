# Chinmay Homework 1 submission

Running analysis.py produces an output like:
```
Using 'Zmay_chr_9-P-94283818.fa' as observational fasta data
lines to get through: 1

    K-mer    |  Theo. P(occurrence)  |  Obs. P(occurrence)
----------------------------------------------------------
Random  1-mers (9192 checks):
----------------------------------------------------------
 A           |   0.2500000000000     |   0.3013489991297
 C           |   0.2500000000000     |   0.2170365535248
 T           |   0.2500000000000     |   0.2598999129678
 G           |   0.2500000000000     |   0.2217145343777
----------------------------------------------------------
Random  2-mers (9191 checks):
----------------------------------------------------------
 AC          |   0.0625000000000     |   0.0572298988141
 TT          |   0.0625000000000     |   0.0808399521271
 AA          |   0.0625000000000     |   0.1026003699271
 GG          |   0.0625000000000     |   0.0566858883691
 TA          |   0.0625000000000     |   0.0549450549451
----------------------------------------------------------
Random  3-mers (9190 checks):
----------------------------------------------------------
 CGC         |   0.0156250000000     |   0.0088139281828
 ATG         |   0.0156250000000     |   0.0199129488575
 TTA         |   0.0156250000000     |   0.0158868335147
 GGA         |   0.0156250000000     |   0.0176278563656
 AGT         |   0.0156250000000     |   0.0147986942329
----------------------------------------------------------
Random  4-mers (9189 checks):
----------------------------------------------------------
 CCAA        |   0.0039062500000     |   0.0097943192948
 TAGC        |   0.0039062500000     |   0.0019588638590
 CTAC        |   0.0039062500000     |   0.0031559473283
 TTTA        |   0.0039062500000     |   0.0050059854173
 TAGA        |   0.0039062500000     |   0.0038089019480
----------------------------------------------------------
Random  5-mers (9188 checks):
----------------------------------------------------------
 GGGTC       |   0.0009765625000     |   0.0004353504571
 CCTCG       |   0.0009765625000     |   0.0006530256857
 CCAGA       |   0.0009765625000     |   0.0003265128428
 CTAGA       |   0.0009765625000     |   0.0008707009142
 ACTCT       |   0.0009765625000     |   0.0013060513714
----------------------------------------------------------
Random  6-mers (9187 checks):
----------------------------------------------------------
 CATGCA      |   0.0002441406250     |   0.0001088494612
 GGTAGG      |   0.0002441406250     |   0.0000000000000
 TGTAGT      |   0.0002441406250     |   0.0005442473060
 CGTGGA      |   0.0002441406250     |   0.0000000000000
 CGCGAG      |   0.0002441406250     |   0.0000000000000
----------------------------------------------------------
Random  7-mers (9186 checks):
----------------------------------------------------------
 ACACGAC     |   0.0000610351562     |   0.0000000000000
 AGCCTAG     |   0.0000610351562     |   0.0000000000000
 CTGTGTG     |   0.0000610351562     |   0.0000000000000
 GTCCCAC     |   0.0000610351562     |   0.0000000000000
 TCACTGA     |   0.0000610351562     |   0.0000000000000
----------------------------------------------------------
Random  8-mers (9185 checks):
----------------------------------------------------------
 CAGGGGAG    |   0.0000152587891     |   0.0000000000000
 GGCGCCGC    |   0.0000152587891     |   0.0000000000000
 GCATCTAG    |   0.0000152587891     |   0.0001088731628
 CGCTCGTA    |   0.0000152587891     |   0.0000000000000
 AAAAGGCA    |   0.0000152587891     |   0.0000000000000
----------------------------------------------------------
Random  9-mers (9184 checks):
----------------------------------------------------------
 CGTCGCCTG   |   0.0000038146973     |   0.0000000000000
 GCTGCCCCA   |   0.0000038146973     |   0.0000000000000
 ACCTTTGTT   |   0.0000038146973     |   0.0000000000000
 ATCGCCTTG   |   0.0000038146973     |   0.0000000000000
 CTCAGCTCT   |   0.0000038146973     |   0.0000000000000
----------------------------------------------------------
Random 10-mers (9183 checks):
----------------------------------------------------------
 CTTGCCGAGT  |   0.0000009536743     |   0.0000000000000
 ACTATACCGG  |   0.0000009536743     |   0.0000000000000
 GCGGTGAGAA  |   0.0000009536743     |   0.0000000000000
 TGCGATTAAG  |   0.0000009536743     |   0.0000000000000
 TCAGTCACAG  |   0.0000009536743     |   0.0000000000000
 ```
 
## interpreting this result:
 - The left column is the K-mer sequence
 - The middle column is the theoretical probability of occurrence in a sequence of k nucleotides. The probability distribution for the bases was assumed to be normal
 - The rightmost column is the observed probability of the k-mer using the file specified at the top.
 
 *The matches found include overlapping matches. For example searching for "AA" in "AAA" produces 2 matches.*
 
## my analysis of the results:
I was sure that the nucleotides in a strand a DNA don't follow a uniform random distribution and the observational data kinda proves it. Some K-mers like 'AA' have 1.5 the odds of occurrence in the observed genome compared to the theoretical probability.
I believe for that case this was due to the existence and presence of the TATA box which act as start points for DNA transcription as 'TT' and 'TA' seem to occur often as well. Pretty interesting to see the differences in theoretical and observed probability.
