seqs = "ATGC"


def complement(seq):
    # doc string
    ''' change nucleotide to it's complement  '''
    new_dict = {"A": "T", "C": "G"}
    empty_str = ''
    for nuc in seq:
        for key, value in new_dict.items():
            if nuc == key:
                empty_str += value
            elif nuc == value:
                empty_str += key
    return empty_str


# IN CASE or producing RNA
#     return empty_str.replace("A", "U")

print(f' [1] + complement : {complement(seqs)}')

def reverse_complemment(seq, init_pos =0):
    dna_reversecomplementary = {"A": "T", "T": "A", "G": "C", "C": "G"}
    return ''.join([dna_reversecomplementary[nuc] for nuc in seq])[::-1]


print(f' [2] + reverse complement : {(reverse_complemment(seqs))}')

#GC content in DNA subseq
gene = "ATGCATGCATGC"


def gc_content(gene):
    return round(gene.count("G") + gene.count("C")) / len(gene) * 100


def gc_content_subseq(gene, k=20):
    ''' gc content in dna sub-sequence length k, k = 20 by default '''
    res = []
    for i in range(0, len(gene)-k+1, k):
        subseq = gene[i: i + k]
        res.append(gc_content(subseq))
    return res


print(gc_content_subseq(gene, k=4))
print(gc_content(gene))
