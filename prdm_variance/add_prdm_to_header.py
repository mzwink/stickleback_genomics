
prdm_genes = ['mecom', 'prdm1a', 'prdm1c', 'prdm2b', 'prdm4', 'prdm8', 'prdm9', 'prdm10', 'prdm12' ,'prdm13', 'prdm14']
directory = '/Volumes/MW_18TB/Madison_Zwink/stickleback_genome/snp_variance_summaries/snp_count_summaries/'

#region_info = '/Volumes/MW_18TB/Madison_Zwink/stickleback_genome/genomic_dna/fq_file_id.txt'
#region_info = open(region_info).readlines()

#region_info_dict = {}

#for value in region_info:
#    value = value.rstrip().split("    ")

#    population = value[0]
#    region = value[3]

#    region_info_dict[population] = [region]


#print(region_info_dict)
for prdm in prdm_genes:

    summary_file = directory + prdm + '_snp_variance.txt'

    output = summary_file.replace(".txt", "_format.txt")
    output = open(output, 'w')

    summary_file = open(summary_file).readlines()

    for line in summary_file:
        if line.startswith('Population'):
            header = line.rstrip().split("\t")

            for info in header:

                if info == 'Population':
                    output.write(info + "\t")

                elif info == header[len(header) -1]:
                    new_header = prdm + "." + info
                    output.write(new_header + "\n")

                else:
                    new_header = prdm + "." + info
                    output.write(new_header + "\t")

        #elif line.startswith('ERR407'):
        #    #output.write(line)
        #    line = line.split("\t")

        #    population = line[0]

        #    region = region_info_dict[population]
        #    for r in region:
        #        region = r

        #    output.write(population + "\t" + region + "\t")

        #    for value in line:
        #        if value.startswith('ERR'):
        #            continue

        #        else:
        #            output.write(value + "\t")


        else:
            output.write(line)
            #line = line.split("\t")

            #for value in line:
            #    if value.startswith('Total'):
            #        output.write(value + "\t" + "NA" + "\t")

            #    else:
            #        output.write(value + "\t")
