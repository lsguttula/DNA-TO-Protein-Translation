codon_table = {
    "ATG": "M",
    "GCC": "A",
    "ATT": "I",
    "GTA": "V",
    "TGG": "W",
    "GGC": "G",
    "CGC": "R",
    "TGA": "*"
}

file = open("sample.fasta", "r")

lines = file.readlines()

dna = ""

for line in lines:
    if not line.startswith(">"):
        dna += line.strip()

protein = ""

for i in range(0, len(dna)-2, 3):
    codon = dna[i:i+3]
    protein += codon_table.get(codon, "X")

print("DNA Sequence:")
print(dna)

print("\nProtein Sequence:")
print(protein)