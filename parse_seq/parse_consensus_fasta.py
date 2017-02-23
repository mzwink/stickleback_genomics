from Bio import SeqIO

def correct_consensus_fasta(consensus_fasta, vcf_file, region):

    output = consensus_fasta.replace('.fasta', '_test.fasta')
    output = open(output, 'w')
    consensus_fasta = SeqIO.parse(open(consensus_fasta), 'fasta')

    fasta_id = ''
    replacement_list = []
    fasta_seq = ''

    vcf_file = open(vcf_file).readlines()

    for fasta in consensus_fasta:
        fasta_id = fasta.id
        fasta_seq = fasta.seq

        #print(fasta[539])
        #print(len(fasta_seq))

    region = region.split(":")

    coordinates = region[1].split("-")

    fasta_id = region[0]
    start = int(coordinates[0]) - 1
    end = int(coordinates[1])


    for variant in vcf_file:
        if variant.startswith('#'):
            continue

        else:
            variant = variant.split("\t")

            fasta = variant[0]
            #Make position base 0
            position = int(variant[1]) -1
            ref_allele = variant[3]
            alt_allele = variant[4].split(',')

            if fasta_id == fasta and position >= start-1 and position <= end:

                if len(alt_allele) > 1:
                    if alt_allele[0] != '<NON_REF>' and len(alt_allele[0]) == 1:

                        target_seq_location = int(position) - int(start)

                        replacement_list.append([target_seq_location, alt_allele[0]])


                    elif len(alt_allele) == 1 and alt_allele == '<NON_REF>':
                        continue

    prev_pos = 0
    counter = 0
    new_consensus = ''
    #print(replacement_list)
    for pos in replacement_list:
        #print(counter)
        position = int(pos[0])
        alt_allele = pos[1]

        if counter < len(replacement_list) -1:
            sub_seq = fasta_seq[prev_pos:position]
            new_consensus += sub_seq
            new_consensus += alt_allele
            prev_pos = position + 1
            counter += 1

        else:
            #print('last part of sequence')
            sub_seq = fasta_seq[prev_pos:position]
            new_consensus += sub_seq
            new_consensus += alt_allele
            end_seq = fasta_seq[position+1:]
            new_consensus += end_seq


    #print(new_consensus[539])
    #print(len(new_consensus))
    new_consensus = str(new_consensus)


    output.write(">" + str(fasta_id) + "\n" + new_consensus + "\n")

######################### MAIN #########################

directory = '/Volumes/MW_18TB/Madison_Zwink/stickleback_genome/genomic_dna/vcf_files/'
#consensus_fasta = str(directory) + 'ERR407002_prdm1a_consensus.fasta'

prdm_list = [['prdm1a', 'scaffold_122:86160-94332'], ['prdm1c', 'groupXVIII:9013111-9022843'], ['prdm2b', 'scaffold_27:3386789-3397946'], ['prdm4', 'groupIV:19741262-19747434'] ,['prdm8', 'groupVI:8320996-8324887'] ,['prdm9', 'groupV:3410473-3415373'], ['prdm10', 'groupI:15504384-15515157'], ['prdm12b', 'groupXIV:5445284-5450247']
, ['prdm13', 'groupXX:3318389-3325634'], ['prdm14','groupXXI:6959347-6964454'], ['mecom', 'groupI:5464852-5489747']]

stickleback_populations = ['ERR407002', 'ERR407006', 'ERR407009', 'ERR407012', 'ERR407025', 'ERR407270', 'ERR407276',
'ERR407291', 'ERR407302', 'ERR407318', 'ERR407319']

for prdm in prdm_list:

    gene = prdm[0]
    region = prdm[1]

    for population in stickleback_populations:

        consensus_fasta = directory + population + "_" + gene + '_consensus.fasta'
        vcf_file = consensus_fasta.replace('_consensus.fasta', '_cV.g.vcf')

        correct_consensus_fasta(consensus_fasta, vcf_file, region)
