from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

#seqio and sequtils are the modules of biopython 
#seqio=input output files
#sequtils= for gc fraction , protein analyser etc

#in the above question they asked which has maximum gc and its id 
max_gc = 0
max_id = ""

# read FASTA file (change filename if needed)
for record in SeqIO.parse("rosalind_gc.fasta", "fasta"):
    gc = gc_fraction(record.seq) * 100  # convert to percentage
#gc fractiin is inbuilt fucntion inside sequtils
  
    if gc > max_gc:
        max_gc = gc
        max_id = record.id

# print result
print(max_id)
print(f"{max_gc:.6f}")
#6f,for round off figues of gc percentage value