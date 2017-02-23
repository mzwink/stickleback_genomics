directory = '/Volumes/MW_18TB/Madison_Zwink/stickleback_genome/prdm_exons/mrna_fasta/'
prdm_genes = ['mecom', 'prdm1a', 'prdm1c', 'prdm2b','prdm4', 'prdm8', 'prdm9', 'prdm10', 'prdm12b' ,'prdm13', 'prdm14']

from Bio import SeqIO

for prdm in prdm_genes:
    fasta_file = directory + prdm + '_mrna.fasta'

    fasta_file = SeqIO.parse(open(fasta_file), 'fasta')

    for fasta in fasta_file:
        fasta_seq = fasta.seq

        print(fasta.id + "\n" + str(len(fasta_seq)))

#correct length
#prdm14
#prdm13
#prdm12b
#prdm10
#prdm2b
#prdm1c
#mecom


#fix
#prdm9 - should be len 2301 (now at 2233)
#prdm8 - should be len 1892 (now at 1521)
#prdm4 - should be len 4173 (now at 2346)
#prdm1a - should be len 2031 (now at 3387)
