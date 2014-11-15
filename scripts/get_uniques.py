#!/usr/bin/python
from Bio import SeqIO
import sys


def remove_dups(infile, outfile):
    handle = open(infile, "rU")
    records = []
    seqs = {}
    for record in SeqIO.parse(handle, "fasta"):
        s = str(record.seq)
        if s in seqs:
            continue #duplicate, skip
        else:
            seqs[s] = True
        records.append(record)
    handle.close()
    
    output_handle = open(outfile, "w")
    SeqIO.write(records, output_handle, "fasta")
    output_handle.close()

if len(sys.argv) != 3:
    print "Please provide infile and outfile as command-line arguments"
else:
    remove_dups(sys.argv[1], sys.argv[2])
