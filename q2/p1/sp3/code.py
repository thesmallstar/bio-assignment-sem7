from Bio import SeqIO
fasta_sequences = SeqIO.parse(open('../data/insulin_human.fasta'), 'fasta')
for fasta in fasta_sequences:
    _id, sequence = fasta.id, str(fasta.seq)
    print("Fasta ID for Human Insulin Gene:", _id) 
    print("The number of ‘GAAT’ sequence repeats in the gene are:", sequence.count('GAAT'))
    
