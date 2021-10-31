from Bio import SeqIO

def getSequencesFromFastaFile(input_file):
    fasta_sequences = SeqIO.parse(open(input_file), 'fasta')
    sequences = []
    for fasta in fasta_sequences:
        _id, sequence = fasta.id, str(fasta.seq)
        sequences.append((_id,sequence))
    return sequences

fasta_sequences = getSequencesFromFastaFile('../data/insulin_human.fasta')
for fasta in fasta_sequences:
    _id, sequence = fasta
    print("Fasta ID for Human Insulin Gene:", _id) 
    print("The number of ‘GAAT’ sequence repeats in the gene are:", sequence.count('GAAT'))