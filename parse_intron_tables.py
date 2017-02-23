
#from Bio import SeqIO

#Use start sites from Ensembl for 

def parse_introns(prdm_gene, directory):
    intron_table = directory + str(prdm_gene) + '_introns.csv'
    reference_file = directory + 'reference_fasta/' + str(prdm_gene) + '_' + chromosome + '.fasta'
    #reference_file = open(reference_file).readlines
    intron_table = open(intron_table).readlines()

    intron_info = []

    for line in intron_table:
        if line.startswith("Name"):
            continue

        else:
            line = line.split(",")

            name = line[0]

            start = ''
            end = ''
            len_intron = 0
            #print(prdm_gene)
            if line[1].startswith("\""):
                start += line[1]

                if line[3].endswith("\""):
                    start += line[2]
                    start += line[3]

                    end += line[4]
                    end += line[5]
                    end += line[6]

                    len_intron = int(line[7])

                elif line[2].endswith("\""):
                    start += line[2]

                    end += line[3]
                    end += line[4]

                    len_intron = int(line[5])

            start = start.replace("\"", '')
            start = int(start)

            end = end.replace("\"", '')
            end = int(end)


            intron_info.append([start, end])


    translate_gdna(intron_info, reference_file)

def translate_gdna(intron_info, reference_file):

    reference_file = open(reference_file).readlines()#SeqIO.parse(open(reference_file), 'fasta')

    seq_info = ''
    ref_start = 0
    ref_end = 0
    reference_sequence = ''

    for fasta in reference_file:
        #print(fasta)
        if fasta.startswith(">group") or fasta.startswith('>scaff'):
            fasta_header = fasta.split(" ")
            seq_info = fasta_header[1]
            seq_info = seq_info.split(':')
            #print(seq_info[0])
            #print(seq_info[1])

            seq_range = seq_info[1].split("-")

            #seq_range = seq_info[1]
            #Set start to base 0
            ref_start = int(seq_range[0])-1
            ref_end = int(seq_range[1])


        else:
            fasta = fasta.rstrip()
            reference_sequence += fasta

        if ref_start > ref_end:
            reference_sequence = reference_sequence[::-1]



    #print(seq_info)
    #print(reference_sequence)
    new_ref_seq = reference_sequence

    for info in intron_info:
        ###prdm1c,prdm4, prdm8 are reversed
        ##re-reversed them
        end_seq = int(ref_end - ref_start)

        start = int(info[0]) #- ref_start
        end = int(info[1]) #- ref_start


        start = start - ref_start
        end = end - ref_start + 1

        #print(seq_info[0])
        #print(start)
        #print(end)

        #print("\nDifference: " + str(ref_end - ref_start) + "\n")
        #print('intron_start: ' + str(start)+ "\n")
        #print('intron_end: ' + str(end) + '\n')

        intron_seq = reference_sequence[start -1:end-1].lower()
        #reference_sequence[start -1:end-1] = intron_seq

        new_end = new_ref_seq[end:end_seq]
        new_start = new_ref_seq[0:start-2]
        #new_ref_seq = new_ref_seq[0:start-2]
        new_intron = intron_seq

        ###Put all together to create new reference sequence

        new_ref_seq = new_start + new_intron + new_end

    print(seq_info[0])
    print(len(new_ref_seq))

    print("###########")

    print(ref_end - ref_start)

    print(new_ref_seq)

        #new_ref_seq += new_ref_seq[end:end_seq]

        #print(new_ref_seq)
        #print(reference_sequence)



        #print(seq_info[0])
        #print(intron_seq)



#####################   MAIN    #####################
prdm_genes = [['mecom', 'groupI'], ['prdm1a', 'scaffold122'], ['prdm1c', 'groupXVIII'], ['prdm2b', 'scaffold27'], ['prdm4', 'groupIV'], ['prdm8', 'groupVI'], ['prdm9', 'groupV'], ['prdm10','groupI'],
['prdm12b', 'groupXIV'], ['prdm13', 'groupXX'] ,['prdm14', 'groupXXI']]

directory = '/Volumes/MW_18TB/Madison_Zwink/stickleback_genome/introns/'

for prdm in prdm_genes:
    prdm_gene = prdm[0]
    chromosome = prdm[1]
    #print(prdm_gene)
    #print(chromosome)

    if prdm_gene == 'prdm13':
        intron_info = []
        reference_file = directory + 'reference_fasta/' + str(prdm_gene) + '_' + chromosome + '.fasta'
        translate_gdna(intron_info, reference_file)

    else:

        parse_introns(prdm_gene, directory)

        ###########Make a parse_intron function##########


            #print("start:" + str(start))
            #print("end: " + str(end))
            #print("length: " + str(len_intron))
