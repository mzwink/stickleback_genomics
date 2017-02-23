###################################################################
######  Create Consensus fasta by parsing vcf viles  ##############
###################################################################

from Bio import SeqIO

###################################################################
######  Parse through fasta files - find variance   ###############
# Input: Reference fasta, list of prdm genes, list of populations #
###################################################################
def parse_ref_fasta(ref_fasta, prdm_list, population_list):

    parse_ref = SeqIO.parse(open(reference_fasta), 'fasta')

    for prdm in prdm_list:
        #print(prdm)
        gene = str(prdm[0])
        region = str(prdm[1])

        for population in stickleback_populations:
            #print(population)
            vcf_file = directory + 'vcf_files/' +str(population) + '_' + str(gene) + '_cV.g.vcf'
            #print(vcf_file)
            parse_variants(vcf_file, region, parse_ref)

###################################################################
###  Parse VCF file - replace reference allele with alt allele  ###
###### Input: VCF file, prdm gene location, reference fasta #######
###################################################################

def parse_variants(vcf_file, region, parse_ref):


    output = vcf_file.replace('_cV.g.vcf', '_consensus.fasta')
    output = open(output, 'w')

    vcf_file = open(vcf_file).readlines()

    replacement_list = []
    target_seq = ''
    fasta_id = ''

    print(region)
    region = region.split(":")

    group = region[0]
    coordinates = region[1].split("-")

    start = int(coordinates[0]) - 1
    end = int(coordinates[1])


    for fasta in parse_ref:
        if fasta.id == group:

            ref_seq = fasta.seq
            target_seq = ref_seq[start:end]

            for variant in vcf_file:
                if variant.startswith('#'):
                    continue

                else:
                    variant = variant.split("\t")

                    fasta_id = variant[0]
                    #Make position base 0
                    position = int(variant[1]) -1
                    ref_allele = variant[3]
                    alt_allele = variant[4].split(',')

                    if fasta_id == group and position >= start-1 and position <= end:

                        if len(alt_allele) > 1:
                            if alt_allele[0] != '<NON_REF>' and len(alt_allele[0]) == 1:

                                target_seq_location = int(position) - int(start)

                                replacement_list.append([target_seq_location, alt_allele[0]])


                            elif len(alt_allele) == 1 and alt_allele == '<NON_REF>':
                                continue

            print(replacement_list)
    consensus_fasta = create_consensus_fasta(target_seq, replacement_list)
    output.write(">" + str(group) + "\n" + consensus_fasta)

###################################################################
######## Write consensus sequence to separate fasta file ##########
####  Input: prdm domain position, list of variance locations  ####
###################################################################

def create_consensus_fasta(target_seq, replacement_list):

    consensus_fasta = ''

    prev_pos = 0
    counter = 0
    for pos in replacement_list:
        counter += 1
        position = pos[0]
        alt_allele = pos[1]

        if counter < len(replacement_list) -1:
            sub_seq = str(target_seq[prev_pos:position])
            consensus_fasta += sub_seq
            consensus_fasta += str(alt_allele)
            prev_pos = position + 1

        else:
            sub_seq = str(target_seq[prev_pos:position])
            consensus_fasta += sub_seq
            consensus_fasta += alt_allele
            end_seq = str(target_seq[position+1:])
            consensus_fasta += sub_seq

    return consensus_fasta


################################### MAIN #######################################
#Initiate directory of required files, create list of prdm genes with location##
#######in Ensembl genome and list of stickleback populations for analysis#######
################################################################################

directory = '/Volumes/MW_18TB/Madison_Zwink/stickleback_genome/genomic_dna/'
reference_fasta = directory + 'Gasterosteus_aculeatus.BROADS1.dna.all.fa'

prdm_list = [['prdm1a', 'scaffold_122:86160-94332'], ['prdm1c', 'groupXVIII:9013111-9022843'], ['prdm2b', 'scaffold_27:3386789-3397946'], ['prdm4', 'groupIV:19741262-19747434'] ,['prdm8', 'groupVI:8320996-8324887'] ,['prdm9', 'groupV:3410473-3415373'], ['prdm10', 'groupI:15504384-15515157'], ['prdm12b', 'groupXIV:5445284-5450247']
, ['prdm13', 'groupXX:3318389-3325634'], ['prdm14','groupXXI:6959347-6964454'], ['mecom', 'groupI:5464852-5489747']]

stickleback_populations = ['ERR407002', 'ERR407006', 'ERR407009', 'ERR407012', 'ERR407025', 'ERR407270', 'ERR407276',
'ERR407291', 'ERR407302', 'ERR407318', 'ERR407319']

parse_ref_fasta(reference_fasta, prdm_list, stickleback_populations)
