from Bio import SeqIO
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt


def getSequencesFromFastaFile(input_file):
    fasta_sequences = SeqIO.parse(open(input_file), 'fasta')
    sequences = []
    sequence_ids = []
    for fasta in fasta_sequences:
        id, sequence = fasta.id, str(fasta.seq)
        sequences.append(sequence)
        sequence_ids.append(id)
    return sequences, sequence_ids


dataPath = "../data/"


def processFile(fileName):
    sequences, sequence_ids = getSequencesFromFastaFile(dataPath+fileName)
    fileName = fileName[0:-6]
    print("Processing File: " + fileName)
    print("Found " + str(len(sequences)) + " Sequences")
    for idx in range(0, len(sequences)):
        sequence = sequences[idx]
        sequence_id = sequence_ids[idx]
        gc_count_percent_store = []

        # blue if gc_count>=60% and red if at_count>=60% else green
        region_type = []
        high_gc_colour = "royalblue"
        low_gc_colour = "red"
        mid_gc_colour = "lightgreen"

        for i in range(0, len(sequence), 200):
            gc_count = 0
            for j in range(i, min(len(sequence), i+200)):
                if(sequence[j] == 'G' or sequence[j] == 'C'):
                    gc_count += 1
            length_region = min(200, len(sequence)-i)
            gc_count_percent_store.append(100*(gc_count/length_region))
            if gc_count >= length_region * 0.6:
                region_type.append(high_gc_colour)
            elif gc_count <= length_region * 0.4:
                region_type.append(low_gc_colour)
            else:
                region_type.append(mid_gc_colour)

        print(gc_count_percent_store)

        plt.bar(list(range(0, len(gc_count_percent_store)*200, 200)),
                gc_count_percent_store, color=region_type, width=200, align="edge")

        colors = {
            "high_gc_region": high_gc_colour,
            "low_gc_region": low_gc_colour,
            "otherwise": mid_gc_colour
        }
        labels = list(colors.keys())
        handles = [plt.Rectangle((0, 0), 1, 1, color=colors[label])
                   for label in labels]

        plt.legend(handles, labels)

        ax = plt.gca()
        ax.set_title(fileName + ': ' + sequence_id)
        ax.set_ylim([0, 100])
        ax.set_xlabel("Neucleotide Region range")
        ax.set_ylabel("GC Content(%)")
        plt.show()

        ax = plt.gca()
        ax.set_title("Frequency Distribution over GC Content(%): " + fileName + ': ' + sequence_id)
        ax.set_ylabel("Frequency")
        ax.set_xlim([0, 100])
        ax.set_xlabel("Range of GC Content(%)")
        plt.hist(gc_count_percent_store, align="mid", color="orange")
        plt.show()




files = [f for f in listdir(dataPath) if isfile(join(dataPath, f))]
for file in files:
    processFile(file)
