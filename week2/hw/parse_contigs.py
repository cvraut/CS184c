import sys
import os, errno

directory = './contigs'
special_chars = {'|','>','<','?','*','"',":","/","\\"}

def sanitize(s):
    for c in special_chars:
        s = s.replace(c,'')
    return s

fasta_file_name = input("Please specify the fasta file to prune: ").strip()
fasta_file = open(fasta_file_name)
contigs_to_save = set()

print("\nPlease enter the contig names to search for (Empty input to end):")
for line in sys.stdin:
    if line.strip() == "":
        break
    contigs_to_save.add(line.strip())

record = False
out_file = None
found = set()
for line in fasta_file:
    line = line.strip()
    if line.startswith('>'):
        if line[1:] in contigs_to_save:
            record = True
            try:
                os.makedirs(directory)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
            out_file = open("{}/{}.fasta".format(directory,sanitize(line)),"w")
            out_file.write(line+'\n')
            found.add(line[1:])
        else:
            record = False
            if out_file:
                out_file.close()
                out_file = None
    elif record:
        out_file.write(line)
fasta_file.close()

print("Found contigs:\n{}".format("\n".join(found)))
print("Could not find contigs:\n{}".format("\n".join(contigs_to_save-found)))