
from xlrd import open_workbook
import math
from Bio import SeqIO

######################    create_text_files   ###########################
### Will open chosen workbook and convert to tab-delimited text file ####
########## Input: Path to excel workbook, list of prdm genes ############
#####   Output: tab-delimited text files for each sheet in workbook #####
#########################################################################

def create_text_files(excel_workbook, prdm_genes):

    excel_workbook = open_workbook(excel_workbook)

    counter = 0

    for gene in prdm_genes:

        sh = excel_workbook.sheets()[counter]
        counter +=1

        num_rows = sh.nrows
        num_columns = sh.ncols

        output = str(gene) + '_exon_info.txt'
        output = open(output, 'w')

        for i in range(0, num_rows):
            for j in range(0, num_columns):
                if j == num_columns -1:
                    output.write(str(sh.cell_value(rowx=i, colx=j)) + "\n")
                else:
                    output.write(str(sh.cell_value(rowx=i, colx=j)) + "\t")

####################   find_exon_locations   ############################
## Parse table from Ensembl to get locations for the exons of the gene ##
######### Input: List of prdm genes, directory to needed files ##########
####   Output: text files with exon sequences and location in genome ####
#########################################################################

def find_exon_locations(prdm_genes, directory):
    for gene in prdm_genes:
        exon_file = directory + gene + "_exon_info.txt"
        output = exon_file.replace('info.txt', 'locations.txt')
        output = open(output, 'w')
        mrna_output = directory + gene + '_mrna_ref.fasta'
        mrna_output = open(mrna_output, 'w')
        mrna_output.write(">" + gene + "_reference\n")

        exon_file = open(exon_file).readlines()
        total_seq = ''
        for line in exon_file:

            if line.startswith("No.") or line.startswith("\t") or line.startswith("\tIntron"):#line.startswith("5'") or line.startswith("3'"):
                continue
            else:
                line = line.split("\t")
                #print(line[1])
                exon_num = line[0]
                seq_type = line[1]
                start = line[2]
                end = line[3]
                sequence = line[7].lstrip().rstrip().replace("\n", "")
                #print(sequence)

                if seq_type.startswith('ENS'):
                    output.write(gene + "\t" + seq_type + "\t" + start + "\t" + end + "\t" + sequence + "\n")
                    #print(sequence)
                    total_seq += sequence
            #print(total_seq)
        total_seq = format_fasta_seq(total_seq)
            #print(total_seq)
        mrna_output.write(total_seq)
        print(">" + gene + "_ref")
        print(len(total_seq))

def format_fasta_seq(complete_sequence):

    seq_len = len(complete_sequence)
    num_iter = math.ceil(seq_len/60)

    format_seq = ''
    for i in range(num_iter):

        if i == num_iter-1:
            start = i*60
            format_line = complete_sequence[start:] + "\n"
            format_seq += format_line
        else:
            start = i*60
            end = start + 60
            format_line = complete_sequence[start:end] + "\n"
            format_seq += format_line

    return format_seq


def create_fasta_with_introns(prdm_genes, directory):
    for prdm in prdm_genes:
        prdm_file = directory + prdm + "_exon_info.txt"
        prdm_file = open(prdm_file).readlines()
        output = directory + prdm+ ".fasta"
        output = open(output, 'w')

        seq_start = 0
        seq_end = 0
        header = ">" +prdm+ ":"
        complete_sequence = ''
        for line in prdm_file:
            if line.startswith("No.") or line.startswith("\t") or line.startswith("\tIntron"):#line.startswith("5'") or line.startswith("3'"):
                continue
            else:

                line = line.split("\t")
                #print(line[1])
                exon_num = line[0]
                seq_type = line[1]
                start = line[2].split(".")
                start = start[0]
                #print(start)
                end = line[3].split(".")
                end = end[0]
                #print(end)
                sequence = line[7].lstrip().rstrip()

                complete_sequence += sequence

                if seq_start == 0:
                    seq_start = int(start)

                elif seq_start > int(start):
                        seq_start = int(start)

                if seq_end < int(end):
                    seq_end = int(end)


        if prdm == 'prdm1a' or prdm == 'prdm4' or prdm == 'prdm1c' or prdm == 'prdm8':
            header += str(seq_end) + "-" + str(seq_start) + ":-1"
        else:
            header += str(seq_start) + "-" + str(seq_end) + ":1"
        output.write(header + "\n")
        #print(complete_sequence)
        complete_sequence = format_fasta_seq(complete_sequence)
        output.write(complete_sequence)


def create_fasta_exons(prdm_genes, directory):
    for prdm in prdm_genes:
        fasta_file = directory+ "gdna_fasta/" + prdm + "_populations_ensembl.fasta"
        fasta_file = SeqIO.parse(open(fasta_file),'fasta')

        output = directory + prdm + "_populations_mrna.fasta"
        output = open(output, 'w')

        exon_locations = directory + 'exon_intron_pos/' + prdm + '_exon_locations.txt'
        exon_locations = open(exon_locations).readlines()

        strand_type = ''
        if prdm == 'prdm1a' or prdm == 'prdm1c'or prdm == 'prdm4'or prdm == 'prdm8':
            strand_type = '-1'

        else:
            strand_type = '1'

        for fasta in fasta_file:
            header = fasta.id
            fasta_seq = fasta.seq

            start_location = 0

            exon_seq = ''

            #if strand_type == '-1':
            #    last_line = exon_locations[len(exon_locations)-1]
            #    last_line = last_line.split("\t")

            #    start_location = last_line[2].split(".")
            #    start_location = int(start_location[0])

            adjuster = 0
            if strand_type == '1':
                adjuster = 1
            else:
                adjuster = int(-1)


            for line in exon_locations:
                if line == exon_locations[0]:
                    line = line.split("\t")

                    start_location = line[2].split(".")
                    start_location = int(start_location[0])
                    pos = line[3].split(".")
                    pos = int(pos[0])
                    #print(start_location)
                    #print(pos)

                    #print(start_location)

                    #print(start_location)
                    #print(pos)

                    start_pos = 0

                    end_pos = (pos - start_location) * adjuster
                    print(end_pos)

                    exon_seq += fasta_seq[start_pos:end_pos+1]
                    #print(fasta_seq[start_pos:end_pos+1])
                    #if prdm == 'prdm4':
                        #print(fasta_seq[start_pos:end_pos] + "\n")
                else:

                    line = line.split("\t")

                    start_pos = line[2].split(".")
                    end_pos = line[3].split(".")

                    start_pos = (int(start_pos[0]) - start_location) * adjuster
                    end_pos = ((int(end_pos[0])) - start_location) * adjuster

                    #print(start_pos)
                    #print(end_pos)
                    #print(start_pos)
                    #print(end_pos)

                    exon_seq += fasta_seq[start_pos:end_pos+1]
                    #print(fasta_seq[start_pos:end_pos+1])
                    #if prdm == 'prdm4':
                        #print(fasta_seq[start_pos:end_pos] + "\n")
                        #print(exon_seq)

            exon_seq = str(exon_seq)
            exon_seq = exon_seq.replace("T", "U")
            exon_seq = format_fasta_seq(exon_seq)
            #print(len(exon_seq))
            output.write(">" + header+"\n")
            output.write(exon_seq + "\n")





def translate_gdna(prdm_genes, directory):
    for prdm in prdm_genes:
        fasta_file = directory + prdm + "_ref.fasta"
        fasta_file = SeqIO.parse(open(fasta_file),'fasta')

        output = directory + prdm + '_mrna_ref.fasta'
        output = open(output, 'w')

        for fasta in fasta_file:

            header = fasta.id
            fasta_seq = fasta.seq


            mrna = ''

            for nucl in fasta_seq:
                #print(nucl)
                if nucl == 'A' or nucl == 'T' or nucl == 'C' or nucl == 'G':
                    mrna += nucl



            if prdm == 'prdm1a' or prdm == 'prdm8' or prdm == 'prdm4':
                strand_type = '-1'
            else:
                strand_type = '1'


            header += ':' + strand_type
            mrna = mrna.replace("T", "U")
            print(len(mrna))

            mrna = format_fasta_seq(mrna)
            output.write(">" + header + "\n" + mrna + "\n")


def translate_consensus_seq(prdm_genes, populations,directory):
    #Should use exon info files to know locations of introns
    #re-adjust snp positions based on new length of fasta w/ only exons

    for prdm in prdm_genes:
        exon_info = directory + prdm + "_exon_locations.txt"
        exon_info = open(exon_info).readlines()

        for pop in populations:
            consensus_file = directory

def create_consensus_files(prdm_genes, directory, populations):

    for prdm in prdm_genes:
        for pop in populations:

            vcf_file = directory + 'vcf_files/' +  pop + '_'+prdm + '_cV.g.vcf'

            reference_fasta = directory + 'gdna_fasta/'+ prdm + '.fasta'
            #output = reference_fasta.replace('.fasta', '_test.fasta')
            output = open(directory + pop + '_' + prdm +'.fasta', 'w')
            reference_fasta = SeqIO.parse(open(reference_fasta), 'fasta')

            fasta_id = ''
            replacement_list = []
            fasta_seq = ''

            vcf_file = open(vcf_file).readlines()

            for fasta in reference_fasta:
                fasta_id = fasta.id
                fasta_seq = fasta.seq

            region = fasta_id.split(":")
            coordinates = region[1].split("-")

            fasta_id = region[0]
            start = int(coordinates[0]) - 1
            end = int(coordinates[1])
            strand_type = region[2]

            #print('fasta_id: ' + str(fasta_id))
            #print('start: ' + str(start))
            #print('end: ' + str(end))
            #print('strand_type: ' + str(strand_type))

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
                    #print(alt_allele)
                    #print(fasta)
                    #print(fasta_id)

                    #if strand_type == '-1' and position <= start-1 and position >= end:

                    #if position >= start-1 and position <= end:
                        #print(alt_allele)
                    if strand_type == '-1' and position <= start-1 and position >= end or strand_type == '1' and position >= start-1 and position <= end:
                        if len(alt_allele) > 1:
                            if alt_allele[0] != '<NON_REF>' and len(alt_allele[0]) == 1:
                                #print(alt_allele[0])
                                target_seq_location = ''
                                if strand_type == '-1':
                                    target_seq_location = int(start) - int(position)
                                    #print(strand_type)
                                    #print(target_seq_location)
                                else:
                                    target_seq_location = int(position) - int(start)
                                    #print(strand_type)
                                    #print(target_seq_location)
                                #print(target_seq_location)

                                replacement_list.append([target_seq_location, alt_allele[0]])


                            elif len(alt_allele) == 1 and alt_allele == '<NON_REF>':
                                continue
            #if prdm == 'prdm4':
            #    print(replacement_list)
            prev_pos = 0
            counter = 0
            new_consensus = ''
            ##print(replacement_list)
            for pos in replacement_list:

                #print(counter)
                position = int(pos[0])
                alt_allele = pos[1]

                if prdm == 'mecom':
                    print(position)
                    print(alt_allele)

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


            ##print(new_consensus[539])
            ##print(len(new_consensus))
            new_consensus = str(new_consensus)
            #print(new_consensus)


            #output.write(">" + str(fasta_id) + "\n" + new_consensus + "\n")


    #Take the vcf files and the reference fasta (w/ introns)
    #Input snps, get rid of introns - figure out where zf domain is


########################## MAIN ########################
prdm_genes = ['mecom', 'prdm1a' ,'prdm1c', 'prdm2b', 'prdm4', 'prdm8', 'prdm9', 'prdm10', 'prdm12b' ,'prdm13', 'prdm14']
reverse_strands = ['prdm1a', 'prdm1c', 'prdm4', 'prdm8']

stickleback_populations = ['ERR407002', 'ERR407006', 'ERR407009', 'ERR407012', 'ERR407025', 'ERR407270', 'ERR407276',
'ERR407291', 'ERR407302', 'ERR407318', 'ERR407319']
#tester_populations= ["prdm2b", "prdm8", "prdm4", "prdm9"]
tester_directory = "/Volumes/MW_18TB/Madison_Zwink/stickleback_genome/prdm_exons/"
tester_populations = ['prdm9', 'prdm8', 'prdm4', 'prdm1a']

excel_workbook = '/Volumes/MW_18TB/Madison_Zwink/stickleback_genome/prdm_exon_spreadsheet.xls'
directory = '/Volumes/MW_18TB/Madison_Zwink/stickleback_genome/prdm_exons/'
exon_dir = '/Volumes/MW_18TB/Madison_Zwink/stickleback_genome/prdm_exons/exon_intron_pos/'

new_directory = '/Volumes/MW_18TB/Madison_Zwink/stickleback_genome/prdm_exons/ref_mrna_seq/'

#find_exon_locations(prdm_genes, exon_dir)
#create_fasta_exons(tester_populations, tester_directory)
#create_fasta_with_introns(prdm_genes, new_directory)
#create_text_files(excel_workbook, prdm_genes)
#find_exon_locations(prdm_genes, directory)
#parse_exon_info(prdm_genes, directory, amino_acid_dict)
#create_fasta_with_introns(prdm_genes, directory)

translate_gdna(prdm_genes, new_directory)

#create_consensus_files(prdm_genes, directory, stickleback_populations)

amino_acid_dict = {
    'UUU': ['F'],
    'UUC': ['F'],
    'UUA': ['L'],
    'UUG': ['L'],
    'CUU': ['L'],
    'CUC': ['L'],
    'CUA': ['L'],
    'CUG': ['L'],
    'AUU': ['I'],
    'AUC': ['I'],
    'AUA': ['I'],
    'AUG': ['M'],
    'GUU': ['V'],
    'GUC': ['V'],
    'GUA': ['V'],
    'GUG': ['V'],
    'UCU': ['S'],
    'UCC': ['S'],
    'UCA': ['S'],
    'UCG': ['S'],
    'CCU': ['P'],
    'CCC': ['P'],
    'CCA': ['P'],
    'CCG': ['P'],
    'ACU': ['T'],
    'ACC': ['T'],
    'ACA': ['T'],
    'ACG': ['T'],
    'GCU': ['A'],
    'GCC': ['A'],
    'GCA': ['A'],
    'GCG': ['A'],
    'UAU': ['Y'],
    'UAC': ['Y'],
    'UGA': ['Stop'],
    'UGG': ['W'],
    'CAU': ['H'],
    'CAC': ['H'],
    'CAA': ['Q'],
    'CAG': ['Q'],
    'AAU': ['N'],
    'AAC': ['N'],
    'AAA': ['K'],
    'AAG': ['K'],
    'GAU': ['D'],
    'GAC': ['D'],
    'GAA': ['E'],
    'GAG': ['E'],
    'UGU': ['C'],
    'UGC': ['C'],
    'CGU': ['R'],
    'CGC': ['R'],
    'CGA': ['R'],
    'CGG': ['R'],
    'AGA': ['R'],
    'AGG': ['R'],
    'AGU': ['S'],
    'AGC': ['S'],
    'GGU': ['G'],
    'GGC': ['G'],
    'GGA': ['G'],
    'GGG': ['G']
 }
