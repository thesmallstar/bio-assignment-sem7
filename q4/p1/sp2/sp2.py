from Bio import SeqIO
import os

inp_file = "../data/beta_amylase_cereus.fasta"


def get_inp_seqs(input_file):
    fasta_sequences = SeqIO.parse(open(os.path.abspath(input_file)), 'fasta')
    sequences = []
    for fasta in fasta_sequences:
        sequences.append(str(fasta.seq))
    return sequences


def main():
    inp_seqs = get_inp_seqs(inp_file)
    for inp_seq in inp_seqs:
        print()
        print("For Gene", inp_seq)
        print("The length of the gene:", len(inp_seq), "nucleotides")
        print("The number of pitches in the gene:", len(inp_seq)/10)


if __name__ == "__main__":
    main()
