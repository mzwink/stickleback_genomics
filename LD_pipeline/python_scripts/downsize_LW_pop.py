import random
import math
import glob

### Iterate remove_seqs number to remove a sequence from fq
### Use random number generator to figure out which sequences to remove_seqs
## Remove both seqs from paired fq files

#Input information for directories
def read_cov_directory():
    read_cov_directory = input("Enter directory with read coverage averages: ")
    if read_cov_directory.endswith("/") == False:
        read_cov_directory += "/"
    return read_cov_directory
def lw_ps_directory():
    lw_ps_directory = input("Enter directory with LW and PS fastq files: ")

    if lw_ps_directory.endswith("/") == False:
        lw_ps_directory += "/"
    return lw_ps_directory

def remove_fq_seq(lw_num_seq, per_difference):

    remove_seqs = int(math.ceil(lw_num_seq - (per_difference * lw_num_seq)))
    remove_lines = {}

    for i in range(remove_seqs):
        random_num = random.randint(0,lw_num_seq)
        file_pos = ''

        if random_num % 4 == 0:
            file_pos = random_num

        else:
            if random_num%4 >= 3:
                while random_num % 4 != 0:
                     random_num += 1

            elif random_num%4 <=2:
                while random_num % 4 != 0:
                    random_num = random_num -1

        file_pos = random_num

        for r in range(file_pos, file_pos+4):
            if r in remove_lines.keys():
                continue
            else:
                remove_lines[r] = 'pos'

    return remove_lines

def parse_LW_avg(LW_avg):

    lw_avg = open(LW_avg).readlines()
    lw_read_cov = 0.0
    for line in lw_avg:
        #if line.startswith(chrom):
        line = line.split("\t")
        lw_read_cov += float(line[1])

    #Average for all chr
    return float(lw_read_cov)/21

def parse_PS_avg(PS_avg):

    ps_avg = open(PS_avg).readlines()
    ps_read_cov = 0.0
    for line in ps_avg:
        #if line.startswith(chrom):
        line = line.split("\t")
        ps_read_cov += float(line[1])

    return float(ps_read_cov)/21


def downsize_LW_pop():
    #r_directory = read_cov_directory()
    #fq_directory = lw_ps_directory()
    r_directory = "/lustre1/mz00685/downsize_read_cov/read_cov/"
    fq_directory = "/lustre1/mz00685/downsize_read_cov/Run1/LW_10_134044-37980194/"

    LW_avg = r_directory + 'LW_avg_read_cov.txt'
    PS_avg = r_directory + 'PS_avg_read_cov.txt'

    lw_avg = parse_LW_avg(LW_avg)
    ps_avg = parse_PS_avg(PS_avg)

    #example: fq_directory = /lustre1/mz00685/downsize_read_cov/Run1/LW_10_134044-37980194/
    #will do this on one pair - remove same reads from its pair
    #files = 34044-10_S10_L001_R1_001.fastq, ...
    fq_files = glob.glob(fq_directory + "*R1*.fastq")

    for fq in fq_files:
        #lw_outputR1_ds1 = fq.replace(".fastq", "_ds1.fastq")
        lw_outputR1 = fq.replace(".fastq", "_ds.fastq")
        fq2 = fq.replace("R1", "R2")
        lw_outputR2= fq2.replace(".fastq", "_ds.fastq")

        fq = open(fq).readlines()

        R1 = fq
        R2 = open(fq2).readlines()

        lw_num_seq = int(len(fq) / 4)

        #per_difference1 = float(lw_read_cov - ps_read_cov)/100
        per_difference = float(1-(ps_avg / lw_avg))

        #removed_lines1 = remove_fq_seq(lw_num_seq, ps_avg, lw_avg, per_difference1)
        removed_lines = remove_fq_seq(lw_num_seq, per_difference)

        output1 = open(lw_outputR1, 'w')
        output2 = open(lw_outputR2, 'w')

        R1_counter = 0
        R2_counter =0

        for line in R1:
            if R1_counter in removed_lines.keys():
                R1_counter += 1

            else:
                output1.write(line)
                R1_counter += 1


        for line in R2:
            if R2_counter in removed_lines.keys():
                R2_counter += 1

            else:
                output2.write(line)
                R2_counter += 1



downsize_LW_pop()
