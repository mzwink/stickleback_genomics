directory = '/lustre1/mz00685/downsize_read_cov/downsized/bam/'

#populations = ['LW', 'PS']
chromosomes = ['chrI', 'chrII', 'chrIII', 'chrIV', 'chrV', 'chrVI', 'chrVII', 'ChrVIII', 'ChrIX',
'ChrX', 'ChrXI', 'ChrXII', 'ChrXIII', 'ChrXIV', 'ChrXV', 'ChrXVI', 'ChrXVII', 'ChrXVIII', 'ChrXIX(sex chr)',
'ChrXX', 'ChrXXI']

output = directory +'LW_avg_readCov_ds.txt'
output = open(output, 'w')
summary_file = directory + 'avg_read_cov.txt'
summary_file = open(summary_file).readlines()


total_cov = 0.0
current_chr = ''
num_populations = 20


for line in summary_file:
    if line.startswith("chr"):
        line = line.rstrip()
        current_chr = line

        if total_cov != 0.0:
            avg_read_cov = float(total_cov / num_populations)
            output.write(current_chr + "\t" + str(avg_read_cov) + "\n")

        total_cov = 0.0

    if line.startswith('LW'):
        line = line.rstrip().split("\t")
        read_cov = float(line[1])
        #print(current_chromosome)

        total_cov += read_cov

    else: continue





        #print(line[0])
