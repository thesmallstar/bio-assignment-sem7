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


def processFile(fileName):
    print("Processing File: " + fileName + "\n")
    sequences = getSequencesFromFastaFile(dataPath+fileName)
    print("Found " + str(len(sequences)) + " Sequences \n")
    count = 1
    for sequence in sequences:
        print("Number of H bonds in Sequence: " str(count) + "is" + str(getHbondsInSequence(sequence)))


files = [f for f in listdir(dataPath) if isfile(join(dataPath, f))]
for file in files:
    processFile(file)
