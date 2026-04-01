"""
Given: A genus name, followed by two dates in YYYY/M/D format.

Return: The number of Nucleotide GenBank entries for the given genus that were published between the dates specified.
"""

from Bio import Entrez
#entrenz is api rpovided by ncbi to retrive parse the file from ncbi 

Entrez.email = "varshbat08@gmail.com"
#email is required to use the api

query="Omphalanthus"
start_data="2004/05/24"
end_data="2009/03/20"
#these are the parameters for the search query,will provide these details

query=f'{query}[Organism] AND ("{start_data}"[PDAT] : "{end_data}"[PDAT])'
handle=Entrez.esearch(db="nucleotide",term=query)
record=Entrez.read(handle)
handle.close()

count=record["Count"]
print(count)