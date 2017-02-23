
from Bio import SeqIO


directory = '/Volumes/MW_18TB/Madison_Zwink/stickleback_genome/genomic_dna/consensus_fasta/'
#consensus_fasta = str(directory) + 'ERR407002_prdm1a_consensus.fasta'

prdm_list = [['prdm1a', 'scaffold_122:86160-94332'], ['prdm1c', 'groupXVIII:9013111-9022843'], ['prdm2b', 'scaffold_27:3386789-3397946'], ['prdm4', 'groupIV:19741262-19747434'] ,['prdm8', 'groupVI:8320996-8324887'] ,['prdm9', 'groupV:3410473-3415373'], ['prdm10', 'groupI:15504384-15515157'], ['prdm12b', 'groupXIV:5445284-5450247']
, ['prdm13', 'groupXX:3318389-3325634'], ['prdm14','groupXXI:6959347-6964454'], ['mecom', 'groupI:5464852-5489747']]

stickleback_populations = ['ERR407002', 'ERR407006', 'ERR407009', 'ERR407012', 'ERR407025', 'ERR407270', 'ERR407276',
'ERR407291', 'ERR407302', 'ERR407318', 'ERR407319']

for prdm in prdm_list:

    prdm_gene = prdm[0]
    region = prdm[1]

    for population in stickleback_populations:

        fasta_file = directory + population + '_' + prdm_gene + '_consensus_wrap.fasta'
        output = fasta_file.replace('wrap.fasta', 'format.fasta')
        output = open(output, 'w')
        fasta_file = SeqIO.parse(open(fasta_file), 'fasta')


        for fasta in fasta_file:

            fasta_header = fasta.id
            fasta_seq = fasta.seq
            new_header = population + "_" + prdm_gene + ":" + fasta_header

            output.write(">" + str(new_header) + "\n" + str(fasta_seq) + "\n")
