# I have produced 2 scripts to manipulate & use multiline fasta files.

###Both python scripts are written to run in python3 only

mult2single.py is a simple light script to convert a multiline fasta file to a single line fasta file.

The way to properly use the script is to use stdin & stdout:
> python mult2single.py < "multline_fasta_file" > "destination_single_line_fasta_file"

Note that the output file would be overwritten and if it used to contain any data, that data will be lost.

parse_contigs.py is a script that reads a multi/single line fasta file and finds the contigs the user is interested in and writes the contigs to an external file in a directory called contigs.

One can run the script & can input the parameters such as filename and contig names through the cli or they can send that input through stdin as shown below:
> python parse_contigs.py < parse_contigs.test.in

Note that the script will create a seperate file for each matching contig found named by the name of the contig (sanitized).
