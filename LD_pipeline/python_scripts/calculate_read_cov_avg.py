directory = '/Volumes/MW_18TB/Alice_Shanfelter/LakeWashington_PugetSound/Bam_files/'

populations = ['LW', 'PS']
chromosomes = ['ChrI', 'ChrII', 'ChrIII', 'ChrIV', 'ChrV', 'ChrVI', 'ChrVII', 'ChrVIII', 'ChrIX', 'ChrX', 'ChrXI', 'ChrXII', 'ChrXIII', 'ChrXIV', 'ChrXV', 'ChrXVI', 'ChrXVII', 'ChrXVIII', 'ChrXIX(sex chr)',
'ChrXX', 'ChrXXI']

for pop in populations:

    num_populations = 20
    output = directory + pop + '_avg_read_cov.txt'
    output = open(output, 'w')
    summary_file = directory + 'Coverage_' + pop + '_sum.txt'
    summary_file = open(summary_file).readlines()

    #current_population = ''

    for chrom in chromosomes:
        total_cov = 0.0

        for line in summary_file:

            if line.startswith('PS') or line.startswith('LW'):
                line = line.rstrip().split("\t")
                current_population = line[0]
                #print(current_population)
                current_chromosome = line[1]
                read_cov = float(line[3])
                #print(current_chromosome)

                if current_chromosome == chrom:
                    total_cov += read_cov


            else:
                line = line.rstrip().split("\t")


                if len(line) > 1:

                    read_cov = ''

                    current_chromosome = line[2]

                    if line[3] == "":
                        read_cov = float(line[4])

                    else:
                        read_cov = float(line[3])

                    #print(read_cov)
                    #print(current_chromosome)
                    # read_cov = line[2]

                    if current_chromosome == chrom:

                        total_cov += read_cov

                else: continue


        avg_read_cov = float(total_cov / num_populations)

        output.write(chrom + "\t" + str(avg_read_cov) + "\n")



        #print(line[0])
