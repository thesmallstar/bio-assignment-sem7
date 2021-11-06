from Bio import SeqIO
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
import numpy as np


def getSequencesFromFastaFile(input_file):
    fasta_sequences = SeqIO.parse(open(input_file), 'fasta')
    sequences = []
    for fasta in fasta_sequences:
        name, sequence = fasta.id, str(fasta.seq)
        sequences.append(sequence)
    return sequences


dataPath = "../data/"

def processFile(fileName):
    print("Processing File: " + fileName)
    sequences = getSequencesFromFastaFile(dataPath+fileName)
    print("Found " + str(len(sequences)) + " Sequences")
    for sequence in sequences:
        region_type=[]
        for i in range(0, len(sequence)-(200+len(sequence) % 200), 200):
            gc_count=0
            for j in range(i, i+200):
                if(sequence[j]=='G' or sequence[j]=='C'):
                    gc_count+=1
            region_type.append(gc_count)
        print(region_type)

        plt.bar(list(range(1, len(sequence)//200)), region_type, width=0.4)
        plt.show()



files = [f for f in listdir(dataPath) if isfile(join(dataPath, f))]
for file in files:
    processFile(file)