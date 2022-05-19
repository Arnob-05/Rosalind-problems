from collections import Counter

DNA_Codons = {
    # 'M' - START, '_' - STOP
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TGT": "C", "TGC": "C",
    "GAT": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "TTT": "F", "TTC": "F",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAT": "H", "CAC": "H",
    "ATA": "I", "ATT": "I", "ATC": "I",
    "AAA": "K", "AAG": "K",
    "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "ATG": "M",
    "AAT": "N", "AAC": "N",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TGG": "W",
    "TAT": "Y", "TAC": "Y",
    "TAA": "_", "TAG": "_", "TGA": "_"
}

seq = "TAATATTGGTACTAC"


def translate_seq(seq, init_pos=0):
    return [DNA_Codons[seq[pos: pos + 3]] for pos in range(init_pos, len(seq)-2, 3)]


print(f'amino acids:{translate_seq(seq , 0)}')


# Finding the frequency of a given amino acid


def codon_freq(seq, amino_acid):
    ''' take a seq and return freq of given amino acid '''
    new_list = []
    for nuc in range(0, len(seq)-2, 3):
        if DNA_Codons[seq[nuc: nuc + 3]] == amino_acid:
            new_list.append(seq[nuc: nuc + 3])

    freq_dict = dict(Counter(new_list))
    total_width = sum(freq_dict.values())
    for num in freq_dict:
        freq_dict[num] = round(freq_dict[num] / total_width, 2)
    return freq_dict


print(f'amino acids freq:{(codon_freq(seq, "Y"))}')


# generating open reading frames
seq = "TAATATTGGTACTAC"
from dna_to_rna import *

def gen_reading_frame(seq):
    ''' generate 6 reading frames of dna including complementary strings'''
    frame = []
    frame.append(translate_seq(seq, 0))
    frame.append(translate_seq(seq, 1))
    frame.append(translate_seq(seq, 2))
    frame.append(translate_seq(reverse_complemment(seq), 0))
    frame.append(translate_seq(reverse_complemment(seq), 1))
    frame.append(translate_seq(reverse_complemment(seq), 2))
    return frame


print(f'orf :')
for frame in gen_reading_frame(seq):
    print(frame)
