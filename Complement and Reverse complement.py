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


# ## IN CASE or producing RNA
#     return empty_str.replace("A", "U")

print(f' [1] + complement : {complement(seqs)}')

dna_reversecomplementary = {"A": "T", "T": "A", "G": "C", "C": "G"}
def reverse_complemment(seq):
    return ''.join([dna_reversecomplementary[nuc] for nuc in seq])[::-1]


print(f' [2] + reverse complement : {(reverse_complemment(seqs))}')