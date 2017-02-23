directory = '/Volumes/MW_18TB/Alice_Shanfelter/LakeWashington_PugetSound/Bam_files/'

populations = ['LW', 'PS']
chromosomes = ['ChrI', 'ChrII', 'ChrIII', 'ChrIV', 'ChrV', 'ChrVI', 'ChrVII', 'ChrVIII', 'ChrIX', 'ChrX', 'ChrXI', 'ChrXII', 'ChrXIII', 'ChrXIV', 'ChrXV', 'ChrXVI', 'ChrXVII', 'ChrXVIII', 'ChrXIX(sex chr)',
'ChrXX', 'ChrXXI']

for pop in populations:

    output = directory + pop + 'avg_read_cov.txt'
    output = open(output, 'w')
    summary_file = directory + 'Coverage_' + pop + '_sum.txt'
    summary_file = open(summary_file).readlines()

    for line in summary_file:
        line = line.rstrip().split("\t")

        print(line[1])
