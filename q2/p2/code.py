inputfile = "dna_sequence.txt"
f = open(inputfile, "r")
dna_seq = f.read()
dna_seq = dna_seq.replace("\n", "")
print("\n.............DNA SEQUENCE.............")
print(dna_seq)

complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
bases = list(dna_seq)
bases = [complement[base] for base in bases]
comp_seq = ''.join(bases)
print("\n.............COMPLEMENTARY SEQUENCE.............")
print(comp_seq)

rna = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
bases = list(comp_seq)
bases = [rna[base] for base in bases]
rna_seq = ''.join(bases)
print("\n.............mRNA SEQUENCE.............")
print(rna_seq)

protein = {"TTT": "F", "CTT": "L", "ATT": "I", "GTT": "V",
           "TTC": "F", "CTC": "L", "ATC": "I", "GTC": "V",
           "TTA": "L", "CTA": "L", "ATA": "I", "GTA": "V",
           "TTG": "L", "CTG": "L", "ATG": "M", "GTG": "V",
           "TCT": "S", "CCT": "P", "ACT": "T", "GCT": "A",
           "TCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
           "TCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
           "TCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
           "TAT": "Y", "CAT": "H", "AAT": "N", "GAT": "D",
           "TAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
           "TAA": "STOP", "CAA": "Q", "AAA": "K", "GAA": "E",
           "TAG": "STOP", "CAG": "Q", "AAG": "K", "GAG": "E",
           "TGT": "C", "CGT": "R", "AGT": "S", "GGT": "G",
           "TGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
           "TGA": "STOP", "CGA": "R", "AGA": "R", "GGA": "G",
           "TGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
           }
protein_sequence = ""
start = 0
end = 0
for i in range(0, len(dna_seq)-(3+len(dna_seq) % 3), 3):
    if protein[dna_seq[i:i+3]] == "STOP":
        end = i
        break

for i in range(0, len(dna_seq)-(3+len(dna_seq) % 3), 3):
    if protein[dna_seq[i:i+3]] == "M":
        start = i
        break
if(start < end):
    for i in range(start, end, 3):
        if protein[dna_seq[i:i+3]] == "STOP":
            break
        protein_sequence += protein[dna_seq[i:i+3]]
    print("\n.............PROTEIN SEQUENCE.............")
    print(protein_sequence)
else:
    print("Protein Sequence does not exist")
