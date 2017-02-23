from Bio import SeqIO

amino_acid_dict = {
 'Phe': ['UUU', 'UUC'],
 'Leu': ['UUA','UUG'],
 'Ile': ['AUU', 'AUC', 'AUA'],
 'Met': ['AUG'],
 'Val': ['GUU', 'GUC', 'GUA', 'GUG'],
 'Ser': ['UCU', 'UCC', 'UCA', 'UCG'],
 'Pro': ['CCU', 'CCC', 'CCA', 'CCG'],
 'Thr': ['ACU', 'ACC', 'ACA', 'ACG'],
 'Ala': ['GCU', 'GCC', 'GCA', 'GCG'],
 'Tyr': ['UAU', 'UAC'],
 'Stop': ['UAA', 'UAG', 'UGA'],
 'His': ['CAU', 'CAC'],
 'Gln': ['CAA', 'CAG'],
 'Asn': ['AAU', 'AAC'],
 'Lys': ['AAA', 'AAG'],
 'Asp': ['GAU', 'GAC'],
 'Glu': ['GAA', 'GAG'],
 'Cys': ['UGU', 'UGC'],
 'Trp': ['UGG'],
 'Arg': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
 'Ser': ['AGU', 'AGC'],
 'Gly': ['GGU', 'GGC', 'GGA', 'GGG']
 }

#Convert cdna to mrna
#Reverse and replace T with U

def create_mrna_sequences(cdna_fasta):
