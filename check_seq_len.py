
from Bio import SeqIO

def check_fasta_seq_len(fasta_file):

    fasta_file = SeqIO.parse(open(fasta_file), 'fasta')

    for fasta in fasta_file:
        fasta_id = fasta.id
        fasta_seq = str(fasta.seq)

        print(fasta_id + "\t" + str(len(fasta_seq)))



directory = "/Volumes/MW_18TB/Alice_Shanfelter/LakeWashington_PugetSound/MEME/Madison_Output/fasta_files/chromosome_fasta/"
#for pop in population:
#    for chrom in chromosomes:
#        fasta_file = pop + ""

#fasta_file = directory + "Ca_L_chrI.fasta"
#check_fasta_seq_len(fasta_file)
seq_line1 ='cttcttctcctcttcctcttccttctccctcttcctcccTGTCGGCGTGTCATCAGATCTGACCAgtgtgtgtgtgtgtt'

print(len(seq_line1))
