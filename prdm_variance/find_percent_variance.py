from xlrd import open_workbook

excel_workbook = open_workbook('/Volumes/MW_18TB/Madison_Zwink/stickleback_genome/consensus_variance.xlsx')
prdm_genes = ['mecom', 'prdm1a', 'prdm1c', 'prdm2b', 'prdm4', 'prdm8', 'prdm9', 'prdm10', 'prdm12' ,'prdm13', 'prdm14']
#samples = 'ERR407002', 'ERR407009', 'ERR407025', 'ERR407012', 'ERR407006', 'ERR407276', 'ERR407291', 'ERR407270', 'ERR407318', 'ERR407302', 'ERR407319'

def create_text_files(excel_workbook, prdm_genes):

    counter = 0

    for gene in prdm_genes:

        sh = excel_workbook.sheets()[counter]
        counter +=1

        num_rows = sh.nrows
        num_columns = sh.ncols

        output = str(gene) + '_consensus_variance.txt'
        output = open(output, 'w')

        for i in range(0, num_rows):
            for j in range(0, num_columns):
                if j == num_columns -1:
                    output.write(str(sh.cell_value(rowx=i, colx=j)) + "\n")
                else:
                    output.write(str(sh.cell_value(rowx=i, colx=j)) + "\t")


def find_variance(directory, file_list):

    #Go through each prdm gene - ex. prdm10, prdm12, ....
    for prdm in file_list:

        output = prdm + "_snp_variance_per.txt"
        output = open(output, 'w')
        output.write('Population' + "\t" )

        prdm_file = directory + prdm + "_consensus_variance.txt"
        prdm_file = open(prdm_file).readlines()

        #Have these reset with every population within every prdm gene?
        ref_allele_list = []
        snp_location = []
        zf_fingers = []
        category = []
        population_info = {}

        #Go through each population - ex. ERR407002, ERR407006, ....
        for row in prdm_file:

            sample_name = ''
            alt_allele_list = []

            if row.startswith('REFERENCE'):
                ref_allele = row.rstrip().split("\t")

                for allele in ref_allele:
                    if len(allele) == 1:
                        ref_allele_list.append(allele)


            elif row.startswith('LOCATION'):
                location = row.rstrip().split("\t")

                for snp in location:

                    if snp != 'LOCATION':
                        if snp != 'PR/SET' and snp != 'ZF_DOMAIN' and snp != 'LOCATION':
                            zf_fingers.append(snp)


                        snp_location.append(snp)


            elif row.startswith('ERR407'):

                consensus_values = row.rstrip().split("\t")
                sample_name = consensus_values[0]

                for alt_allele in consensus_values:
                    if len(alt_allele) < 3:
                        #print(alt_allele)
                        alt_allele_list.append(alt_allele)


                zf_fingers = set(zf_fingers)
                category = ['PR/SET', 'ZF_DOMAIN']


                #Add zinc fingers to the category list
                max_zf_finger = 0

                for zf in zf_fingers:

                    zf_num = zf.replace("ZF", "")
                    zf_num = int(zf_num)

                    if zf_num > max_zf_finger:
                        max_zf_finger = zf_num

                for i in range(1, max_zf_finger + 1):
                    category.append('ZF' + str(i))

                #print(sample_name)
                #print(category)



                for location in category:
                    corresponding_location_pos = []
                    #Go through each category, find where to look for snps that fall in region
                    for i in range(0, len(snp_location)):
                        # NEED ANOTHER FOR LOOP

                        if snp_location[i] == location:
                            #print(location)
                            #print(snp_location[i])
                            #print(i)
                            corresponding_location_pos.append(i)

                    non_match_counter = 0
                    snp_count = 0
                    total_alleles = 0#len(ref_allele_list)
                    snp_var_percentage = 0

                    #####TOTAL ALLELE NUM OFF #######

                    for pos in corresponding_location_pos:
                        ref_allele = ref_allele_list[pos]
                        alt_allele = alt_allele_list[pos]

                        if len(corresponding_location_pos) == 0:

                            print(corresponding_location_pos)
                        #print(len(corresponding_location_pos))


                        total_alleles = len(corresponding_location_pos)

                        if total_alleles > 0:
                            if ref_allele != alt_allele and alt_allele != 'NA':
                                non_match_counter += 1

                    if total_alleles > 0:
                        snp_count = non_match_counter

                    else:
                        snp_count = 0

                    if snp_count != 0:
                        snp_var_percentage = round(float(snp_count/total_alleles) * 100, 2)

                    count_percentage = str(snp_var_percentage) + "%" #+ ", " + str(snp_var_percentage) + "%"

                    if snp_count == 0:
                        count_percentage = 0
                    #print(location)
                    #print(snp_count)

                    if sample_name in population_info.keys():
                        population_info[sample_name].append([location, count_percentage, total_alleles])

                    else:
                        population_info[sample_name] = [[location, count_percentage, total_alleles]]

                    ####RESET VARIABLES#####
                    non_match_counter = 0
                    snp_count = 0
                    #total_alleles = 0#len(ref_allele_list)
                    snp_var_percentage = 'NA'



        samples = ['ERR407002', 'ERR407009', 'ERR407025', 'ERR407012', 'ERR407006', 'ERR407276', 'ERR407291', 'ERR407270', 'ERR407318', 'ERR407302', 'ERR407319']
        samples = sorted(samples)
        #print(samples)


        for domain in category:
            if domain == category[len(category) -1]:
                output.write(domain + "\n")
            else:
                output.write(domain + "\t")

        for population in samples:
            output.write(population + "\t")
            output_info = population_info[population]
            #print(population)
            #for i in range(0, len(category)):
            #    print(output_info[i])

            total_snp_counts = []
            for value in output_info:
                loc = value[0]
                count = value[1]
                total = value[2]

                #print(loc)
                #print(count)
                #print(total)
                total_snp_counts.append(total)

                output.write(str(count)  + "\t")

                if value == output_info[len(output_info) -1]:
                    output.write("\n")

        output.write("Total_SNP_counts" + "\t")

        for snp_count in total_snp_counts:
            output.write(str(snp_count) + "\t")

        output.write("\n")

        #print(prdm)
        #print(population_info['ERR407002'])


######################### Main ###############################
directory = '/Volumes/MW_18TB/Madison_Zwink/stickleback_genome/genomic_dna/prdm_consensus_variance/'
#create_text_files(excel_workbook, prdm_genes)
find_variance(directory, prdm_genes)



####################################################################
#mecom=excel_workbook.sheets()[0]
#prdm1a=excel_workbook.sheets()[1]
#prdm1c=excel_workbook.sheets()[2]
#prdm2b=excel_workbook.sheets()[3]
#prdm4=excel_workbook.sheets()[4]
#prdm8=excel_workbook.sheets()[5]
#prdm9=excel_workbook.sheets()[6]
#prdm10=excel_workbook.sheets()[7]
#prdm12=excel_workbook.sheets()[8]
#prdm13=excel_workbook.sheets()[9]
#prdm14=excel_workbook.sheets()[10]
