inputfile = "dna_sequence_2.txt"
f = open(inputfile, "r")
dna_seq = f.read()
dna_seq = dna_seq.replace("\n", "")
dna_seq = dna_seq.replace("N", "")
print("\n.............DNA SEQUENCE.............\n")
print(dna_seq)

complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
bases = list(dna_seq)
bases = [complement[base] for base in bases]
comp_seq = ''.join(bases)
print("\n.............COMPLEMENTARY SEQUENCE.............\n")
print(comp_seq)

rna = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
bases = list(comp_seq)
bases = [rna[base] for base in bases]
rna_seq = ''.join(bases)
print("\n.............mRNA SEQUENCE.............\n")
print(rna_seq)

protein = {"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
           "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
           "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
           "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
           "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
           "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
           "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
           "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
           "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
           "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
           "UAA": "STOP", "CAA": "Q", "AAA": "K", "GAA": "E",
           "UAG": "STOP", "CAG": "Q", "AAG": "K", "GAG": "E",
           "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
           "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
           "UGA": "STOP", "CGA": "R", "AGA": "R", "GGA": "G",
           "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
           }
protein_sequence = ""
start = 0
end = 0
j = 0
i = 0

while(i < len(rna_seq)):
    if i+3 < len(rna_seq):
        if protein[rna_seq[i:i+3]] == "M":
            start = i
            for j in range(start, len(rna_seq), 3):
                if j+3 < len(rna_seq):
                    if protein[rna_seq[j:j+3]] == "STOP":
                        end = j
                        break

            for k in range(start, end, 3):
                protein_sequence += protein[rna_seq[k:k+3]]
            i = end
    i += 1

print("\n.............PROTEIN SEQUENCE.............\n")
print(protein_sequence)
