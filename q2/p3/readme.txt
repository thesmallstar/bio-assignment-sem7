Step 1: Downloading the FASTA sequence and PDB format files from https://www.rcsb.org/structure/3W7Y

Step 2: Identify the secondary structure in the PDB file. (Lines 447-457)
HELIX    1   1 GLY A    1  SER A    9  1                                   9    
HELIX    2   2 SER A   12  ASN A   18  1                                   7    
HELIX    3   3 GLY B    8  GLY B   20  1                                  13    
HELIX    4   4 GLU B   21  GLY B   23  5                                   3    
HELIX    5   5 ILE C    2  CYS C    7  1                                   6    
HELIX    6   6 SER C   12  GLU C   17  1                                   6    
HELIX    7   7 ASN C   18  CYS C   20  5                                   3    
HELIX    8   8 GLY D    8  GLY D   20  1                                  13    
HELIX    9   9 GLU D   21  GLY D   23  5                                   3    
SHEET    1   A 2 PHE B  24  TYR B  26  0                                        
SHEET    2   A 2 PHE D  24  TYR D  26 -1  O  PHE D  24   N  TYR B  26

We can also use an online tool to retrieve it in the dssp file format from here: https://www3.cmbi.umcn.nl/xssp/

The pictures visualising the secondary structure is also present in the folder. 

For further analysis visit: https://www.rcsb.org/3d-sequence/3W7Y

Step 3: Upload the FASTA sequences one by one in the FASTA tool: https://www.ebi.ac.uk/Tools/sss/fasta/
The Query sequence is run against the database UniProtKB/Swiss-Prot (The manually annotated section of UniProtKB)
BLOSUM50 Similarity Scoring Matrix is used
Score for Gap Open: -10
Score for Gap Extension: -2
K-Tup: 2

Step 4: Analyze the results.