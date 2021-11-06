from typing import List
from Bio import SeqIO

inp_file = "../data/input.fasta"


def get_inp_seqs(input_file):
    fasta_sequences = SeqIO.parse(open(input_file), 'fasta')
    sequences = []
    for fasta in fasta_sequences:
        sequences.append(str(fasta.seq))
    return sequences


def get_reverse_complement(inp_seq):
    rev_seq = inp_seq[::-1]
    rev_comp_seq = ''
    comp_nuc = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }
    for nucleotide in rev_seq:
        rev_comp_seq = rev_comp_seq + comp_nuc[nucleotide]
    return rev_comp_seq


def main():
    inp_seqs: List[str] = get_inp_seqs(inp_file)
    print("The reversed complement of the sequences are:")
    for inp_seq in inp_seqs:
        print("----------------------------------------------")
        print(get_reverse_complement(inp_seq))
        print("----------------------------------------------")


if __name__ == "__main__":
    main()
