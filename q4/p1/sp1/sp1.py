def get_inp_seqs():
    seq = input("Enter the sequence: ")
    return [seq]


def main():
    inp_seqs = get_inp_seqs()
    for inp_seq in inp_seqs:
        print()
        print("For Gene", inp_seq)
        print("The length of the gene:", len(inp_seq), "nucleotides")
        print("The number of pitches in the gene:", len(inp_seq)/10)


if __name__ == "__main__":
    main()
