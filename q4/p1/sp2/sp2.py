from typing import List


def get_inp_seqs():
    seq = input("Enter the sequence: ")
    return [seq]


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
    inp_seqs: List[str] = get_inp_seqs()
    print("The reversed complement of the sequences are:")
    for inp_seq in inp_seqs:
        print(get_reverse_complement(inp_seq))


if __name__ == "__main__":
    main()
