
########### Prdm gene length #############
##### Input: directory, prdm genes #######
#Output: Prints sequence length to screen#
##########################################

def output_fasta_len(directory, prdm_genes):

    from Bio import SeqIO

    for prdm in prdm_genes:
        fasta_file = directory + prdm + '_mrna.fasta'

        fasta_file = SeqIO.parse(open(fasta_file), 'fasta')

        for fasta in fasta_file:
            fasta_seq = fasta.seq

            print(fasta.id + "\n" + str(len(fasta_seq)))


######################## Main #######################

directory = '/Volumes/MW_18TB/Madison_Zwink/stickleback_genome/prdm_exons/mrna_fasta/'
prdm_genes = ['mecom', 'prdm1a', 'prdm1c', 'prdm2b','prdm4', 'prdm8', 'prdm9', 'prdm10', 'prdm12b' ,'prdm13', 'prdm14']
