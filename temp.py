
from Bio import SeqIO

fasta_sequences = SeqIO.parse(open("/home/doginono/Desktop/ElifinAkilAlmazKorkusu/hsv 2 sequence.fasta"),'fasta')
with open("/home/doginono/Desktop/ElifinAkilAlmazKorkusu/output_file") as out_file:
    for fasta in fasta_sequences:
        name, sequence = fasta.id, str(fasta.seq)
        print(sequence)