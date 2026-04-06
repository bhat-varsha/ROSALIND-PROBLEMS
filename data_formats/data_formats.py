from Bio import Entrez
from Bio import SeqIO

# Always set email 
Entrez.email = "varshbhat08@gmail.com"

# Given IDs,keep it is as empty string , download the dataset from website rosalind
ids = ["JX462670", "JQ796071", "JX475048", "NM_001194889", "JX308821", "JX317645", "JX069768", "NM_001081821", "JN573266", "JX445144"]

# Fetch FASTA data
handle = Entrez.efetch(db="nucleotide", id=ids, rettype="fasta")

# Parse records
records = list(SeqIO.parse(handle, "fasta"))

# Find shortest sequence
shortest = min(records, key=lambda x: len(x.seq))
#here we use list comprehension using lamda function 

# Print in FASTA format
print(">" + shortest.description)
print(shortest.seq)