print("Enter the amino acid sequence in single alphabet format")
# Example protein sequence: MKNQFQYCCIVILSVVMLFVSLLIPQASSAAVNGKGMNPDYKAYLMAPLKKIPEVTNWETFENDLRWAKQH
input_protein_sequence = str(input())
total_amino_acids = len(input_protein_sequence)
polar_amino_acids = {'N': [], 'D': [], 'Q': [], 'E': [],
                     'H': [], 'K': [], 'S': [], 'T': [], 'C': [], 'P': []}

for i in range(0, len(input_protein_sequence)):
    if input_protein_sequence[i] in polar_amino_acids:
        polar_amino_acids[input_protein_sequence[i]].append(i)

total_polar_amino_acids = 0
for k in polar_amino_acids:
    total_polar_amino_acids += len(polar_amino_acids[k])

percent_polar = (total_polar_amino_acids/total_amino_acids)*100
print("Percentage of polar amino acids = ", percent_polar, "\n")
print("Positions of polar amino acids:")
for k in polar_amino_acids:
    print(k, ": ")
    for pos in polar_amino_acids[k]:
        print(pos+1, end=" ")
    print("\n")
