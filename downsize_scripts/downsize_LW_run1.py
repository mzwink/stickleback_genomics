import random
import math
import glob

### Iterate remove_seqs number to remove a sequence from fq
### Use random number generator to figure out which sequences to remove_seqs
## Remove both seqs from paired fq files

#Input information for directories
#Optional
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

def remove_fq_seq(lw_file_len, lw_num_seq, per_difference):

    remove_seqs = int(math.ceil(lw_num_seq * per_difference))
    remove_lines = {}
    print(remove_seqs)

    for i in range(remove_seqs):
        random_num = random.randint(0,lw_file_len)

        #find a num % 4 ==0 to get beginning of seq
        if random_num % 4 == 0:
            continue
        else:
            if random_num%4 >= 3:
                while random_num % 4 != 0:
                     random_num += 1

            elif random_num%4 <=2:
                while random_num % 4 != 0:
                    random_num = random_num -1

        for r in range(random_num, random_num+4):
            if r in remove_lines.keys():
                continue
            else:
                remove_lines[r] = 'pos'
    #Return dictionary of positions for easy lookup
    print(len(remove_lines.keys()))
    return remove_lines

def parse_LW_avg(LW_avg):

    lw_avg = open(LW_avg).readlines()
    lw_read_cov = 0.0
    for line in lw_avg:
        line = line.split("\t")
        lw_read_cov += float(line[1])

    #Average for all chr
    return float(lw_read_cov)/21

def parse_PS_avg(PS_avg):

    ps_avg = open(PS_avg).readlines()
    ps_read_cov = 0.0
    for line in ps_avg:
        line = line.split("\t")
        ps_read_cov += float(line[1])

    return float(ps_read_cov)/21


def downsize_LW_pop():
    #r_directory = read_cov_directory()
    #fq_directory = lw_ps_directory()
    directory = "/lustre1/mz00685/downsize_read_cov/Run1/"
    fq_directories = glob.glob(directory + "LW*/")

    r_directory = "/lustre1/mz00685/downsize_read_cov/read_cov/"

    LW_avg = r_directory + 'LW_avg_read_cov.txt'
    PS_avg = r_directory + 'PS_avg_read_cov.txt'

    lw_avg = parse_LW_avg(LW_avg)
    ps_avg = parse_PS_avg(PS_avg)
    print(lw_avg)
    print(ps_avg)

    print("Parsed averages.")

    #example: fq_directory = /lustre1/mz00685/downsize_read_cov/Run1/LW_10_134044-37980194/
    #Will make a list of all R1 files - take same reads from paired file
    #files = 34044-10_S10_L001_R1_001.fastq, ...

    for lw_dir in fq_directories:
        fq_files = glob.glob(lw_dir + "*R1*.fastq")

        for fq in fq_files:
            print(fq)

            #R1 file downsized
            lw_outputR1 = fq.replace(".fastq", "_ds.fastq")
            fq2 = fq.replace("R1", "R2")
            #R2 file downsized
            lw_outputR2= fq2.replace(".fastq", "_ds.fastq")

            R1 = open(fq).readlines()
            R2 = open(fq2).readlines()
            print("Read fastq file.")

            #Number of reads in file
            lw_num_seq = int(len(R1) / 4)
            lw_file_len = int(len(R1))

            print("Number of sequences: " + str(lw_num_seq))
            print("Number of lines in file: " + str(lw_file_len))

            #Change this value to choose how many reads to remove
            per_difference = float(.43)
            print("Percentage of reads to remove: " + str(per_difference))
            print("Number of reads to remove: " + str(int(math.ceil(lw_num_seq * per_difference))))

            #dictionary of reads to remove
            removed_lines = remove_fq_seq(lw_file_len, lw_num_seq, per_difference)
            print("Found lines to remove.")

            output1 = open(lw_outputR1, 'w')
            output2 = open(lw_outputR2, 'w')

            #Want base 1 for removing lines
            R1_counter = 0
            R2_counter = 0

            for line in R1:
                if R1_counter in removed_lines.keys():
                    R1_counter += 1
                    print("Removing line from R1 fastq.")

                else:
                    output1.write(line)
                    R1_counter += 1


            for line in R2:
                if R2_counter in removed_lines.keys():
                    R2_counter += 1
                    print("Removing line from R2 fastq.")

                else:
                    output2.write(line)
                    R2_counter += 1



downsize_LW_pop()
