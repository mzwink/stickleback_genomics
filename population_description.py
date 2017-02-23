directory = '/Volumes/MW_18TB/Madison_Zwink/stickleback_genome/genomic_dna/snp_variance_summaries/'
sample_info = '/Volumes/MW_18TB/Madison_Zwink/stickleback_genome/genomic_dna/fq_file_id.txt'
prdm_genes = ['mecom', 'prdm1a', 'prdm1c', 'prdm2b', 'prdm4', 'prdm8', 'prdm9', 'prdm10', 'prdm12' ,'prdm13', 'prdm14']



for prdm in prdm_genes:
    population_variance = directory + prdm + '_snp_variance.txt'

    output = population_variance.replace('.txt', '_final.txt')
    output = open(output, 'w')

    sample_info = open(sample_info).readlines()
    variance_info = open(population_variance).readlines()
    sample_dict = {}

    for sample in sample_info:

        sample = sample.rstrip()
        sample = sample.split("    ")
        #print(sample)

        sample_name = sample[0]
        #sample_id = sample[1]
        #sex = sample[2]
        population = sample[3]

        sample_dict[sample_name] = [population]

    for variance in variance_info:

        if variance.startswith('Population'):
            variance = variance.rstrip().split('\t')

            print(variance[0])
            header = variance

            for value in header:

                if value == ('Population'):
                    output.write(value + "\tRegion\t")

                elif value == (header[len(header) -1]):
                    output.write(value + "\n")

                else:
                    output.write(value + "\t")

            output.write("\n")

        elif variance.startswith("Total"):
            output.write(variance + "\n")
        else:
            variance = variance.rstrip()
            variance = variance.split("\t")
            #print(variance[0])
            sample_name = variance[0]

            population_info = sample_dict[sample_name]
            region = population_info[0]
            #print(population_info[0])
            #print(population_info[1])
            #print(population_info[2])

            #sample_id = population_info[0]
            #sex = population_info[1]
            #population = population_info[2]

            for v in variance:
                if v == sample_name:
                    output.write(variance[0] + "\t" + region + "\t")
                else:
                    output.write(v + "\t")

            output.write("\n")
