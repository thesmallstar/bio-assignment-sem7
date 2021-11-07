from Bio import SeqIO
from os import listdir
from os.path import isfile, join


def getSequencesFromFastaFile(input_file):
    fasta_sequences = SeqIO.parse(open(input_file), 'fasta')
    sequences = []
    for fasta in fasta_sequences:
        name, sequence = fasta.id, str(fasta.seq)
        sequences.append(sequence)
    return sequences


dataPath = "../data/"


def getHbondsInSequence(sequence):
    countA = 0
    countG = 0
    countC = 0
    countT = 0

    for nucleotide in sequence:
        if nucleotide == 'A':
            countA = countA + 1
        if nucleotide == 'G':
            countG = countG + 1
        if nucleotide == 'C':
            countC = countC + 1
        if nucleotide == 'T':
            countT = countT + 1

    return (countG+countC)*3 + (countA + countT)*2


def processFile(fileName):
    print("Processing File: " + fileName)
    sequences = getSequencesFromFastaFile(dataPath+fileName)
    print("Found " + str(len(sequences)) + " Sequence(s)")
    count = 1
    for sequence in sequences:
        print("Number of H bonds in Sequence " + str(count) +
              " is " + str(getHbondsInSequence(sequence)) + "\n")


files = [f for f in listdir(dataPath) if isfile(join(dataPath, f))]
for file in files:
    processFile(file)
