from Bio import SeqIO
from Bio.Seq import Seq

def get_proteins(seq):
    proteins = set()
    
    # check all 3 reading frames
    for i in range(3):
        translated = seq[i:].translate()
        
        # split at stop codons
        parts = translated.split("*")
        
        for part in parts:
            # find all proteins starting with M
            for j in range(len(part)):
                if part[j] == "M":
                    proteins.add(part[j:])
    
    return proteins


# read FASTA
record = SeqIO.read("rosalind_orf.txt", "fasta")
dna = record.seq

# forward + reverse complement
all_proteins = set()
all_proteins.update(get_proteins(dna))
all_proteins.update(get_proteins(dna.reverse_complement()))

# print results
for p in all_proteins:
    print(p)