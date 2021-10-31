from Bio import SeqIO

input_file = "input.fasta"
fasta_sequences = SeqIO.parse(open(input_file), 'fasta')

with open(output_file) as out_file:
    for fasta in fasta_sequences:
        name, sequence = fasta.id, str(fasta.seq)
        print(sequence)
