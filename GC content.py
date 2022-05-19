gene = "ATGCATGC"

g = 0
a = 0
c = 0
t = 0

for line in gene:
    line = line.lower()
    for char in line:
        if char == "g":
            g += 1
        if char == "a":
            a += 1
        if char == "c":
            c += 1
        if char == "t":
            t += 1
print("number of g's " + str(g))
print("number of a's " + str(a))
print("number of c's " + str(c))
print("number of t's " + str(t))

# convert to floating point (0.)

gc = (g + c + 0.) / (a+t+g+c+0.)

print("gc content: " + str(gc))

# another method


def gc_content(gene):
    '''  amount of G and G in a dna or rna seq  '''
    return round((gene.count("G") + gene.count("C")) / len(gene) * 100)


print(f'gc content : {gc_content(gene)}%')


# GC content in DNA subseq
gene = "ATGCATGCATGC"
def gc_content_subseq(gene, k=20):
    ''' gc content in dna sub-sequence length k, k = 20 by default '''
    res = []
    for i in range(0, len(gene)-k+1, k):
        subseq = gene[i: i + k]
        res.append(gc_content(subseq))
    return res

print( gc_content_subseq(gene, k=4))



#  highest GC content in multiple strings

##1/ Reading data from fasta files.

def readfile(filepath):
    ''' reading a file and returning a list of files'''
    with open(filepath, "r") as f:
        return [l.strip() for l in f.readlines()]


def gc_content(gene):
    '''  amount of G and G in a dna or rna seq  '''
    return ((gene.count("G") + gene.count("C")) / len(gene) * 100)


# storing data in a list
Fasta_file = readfile("rosalind_gc.txt")

# dictionary for leves and data
Fasta_dict = {}

# strings for holding current label
Fasta_lebel = ""


print(Fasta_file)




# converting fasta file into a dictionary
for line in Fasta_file:
    if '>' in line:
        Fasta_lebel = line
        Fasta_dict[Fasta_lebel] = ""
    else:
        Fasta_dict[Fasta_lebel] += line


#generate a new dict for GC content

Result_dict = {key : gc_content(value) for key,value in Fasta_dict.items()}


print(Result_dict)

# looking for max GC values in values() in dict
# get allows you to specify a default value if the key does not exist.

max_GC = max(Result_dict, key = Result_dict.get)


# printing rosalind format result

print(f'{max_GC[1:]}\n{Result_dict[max_GC]}')





