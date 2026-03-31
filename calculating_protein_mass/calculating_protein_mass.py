from Bio.SeqUtils import molecular_weight
protein = "SKADYEK"
mw = molecular_weight(protein, seq_type="protein")
print(mw)