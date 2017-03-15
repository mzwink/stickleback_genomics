############# find_seq_len ##############
########## Input: vcf file ##############
#Output: Length from 1st snp to last snp#
#########################################

def find_seq_len(vcf_file):

    vcf_file = open(vcf_file).readlines()

    start_pos = 0
    end_pos = 0
    seq_length = 0
    for line in vcf_file:
        if line.startswith("#"):
            continue
        else:
            #print(line)
            line = line.split("\t")
            chrom = line[0]
            pos = int(line[1])


            if start_pos == 0:
                start_pos = pos

            elif start_pos != 0 and start_pos > pos:
                start_pos = pos

            if pos > end_pos:
                end_pos = pos


    seq_length = end_pos - start_pos
    #print(seq_length)
    return seq_length

########### Calcualte Avg Theta ###########
#### Input: directory, populations, chr ###
#Output: Text file of avg theta values for#
#### for each population and chromosome ###
###########################################

def calculate_avg_theta(directory, population, chromosomes):

    output = directory + 'avg_theta.txt'
    output = open(output, 'w')

    for pop in population:
        for chrom in chromosomes:

            vcf_file = directory + pop + '_jG_' + chrom + '_phased.vcf'
            seq_len = find_seq_len(vcf_file)

            convert_sum = directory + 'convert_sum/'+ pop + '_' + chrom + '_conSum.txt'
            convert_sum = open(convert_sum).readlines()

            theta = 0.0
            for line in convert_sum:
                if line.startswith('Watterson theta'):
                    line = line.split('=')
                    theta = line[1].rstrip().lstrip()
                    theta = float(theta)

            avg_theta = float(theta/seq_len)

            output.write(pop + '_' + chrom + "\t" + str(avg_theta) +"\n")


############################ MAIN ##############################

directory="/lustre1/mz00685/LD_pipeline/vcf/phased_vcf/"
population = ["Ca_L", "Lm_M", "Kob_M", "Ran_M", "Lm_M", "No_L", "G2_L"]
chromosomes = ["chrXXI", "chrXX", "chrXIX", "chrXVIII", "chrXVII", "chrXVI", "chrXV", "chrXIV", "chrXIII", "chrXII",
"chrXI", "chrX", "chrIX", "chrVIII", "chrVII","chrVI", "chrV", "chrIV", "chrIII", "chrII", "chrI"]

calculate_avg_theta(directory, population, chromosomes)
