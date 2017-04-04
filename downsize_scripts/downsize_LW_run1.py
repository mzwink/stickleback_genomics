import random
import glob
from Bio import SeqIO

#################################################################################
##### Downsize Lake Washington read coverage to match Puget Sound coverage ######
##### Input: Diretory for Lake Washington files (On indiviudal Runs)
##### Input: Number of reads for each individual in LW and PS populations
#           (Format shown below)
##### Output: Downsized fastq file (LW_#_R[1/2]_001_ds.fastq)
#################################################################################
########################## File = Run#_num_reads.txt : ##########################
#       Indiv  LW        PS        Diff
#       1      11915632  9407614   2508018
#       2      14112430  8329780   5782650
#       3      12456006  7064413   5391593
#################################################################################

###########  Enter directory for LW/PS Run  ################
## Will take input path to find LW fastq files (optional) ##
############################################################
def lw_ps_directory():
    lw_ps_directory = input("Enter directory with LW and PS fastq files: ")

    if lw_ps_directory.endswith("/") == False:
        lw_ps_directory += "/"
    return lw_ps_directory


######## Remove fastq identifiers from array  #############
#### Input: Shuffled array of fastq identifiers ###########
# Input: Number of reads to remove based on num_reads file#
#### Output: New array with identifiers that will be used #
#######   to determine reads that are copied to output ####
###########################################################
def remove_fq_seq(random_seq_identifier, num_reads_remove):
    for i in range(num_reads_remove):
        random_seq_identifier.pop(1)

    return random_seq_identifier

###########  Parse num_reads txt file  ###############
########## finds number of reads to remove ###########
##########   Input: Run#_num_reads.txt      ##########
##########   Input: Individual number       ##########
######################################################
def parse_read_counts(read_info_file, indiv_pop_num):
    num_reads = open(read_info_file).readlines()
    indiv_pop = indiv_pop_num

    remove_reads = 0
    for line in num_reads:
        line = line.split("\t")

        indiv = int(line[0])
        value = int(line[3])
        if indiv == indiv_pop:
            remove_reads = value

    return remove_reads


##############  Downsize LW fastq files ###############
#### Takes path to fq files and read count text file #
#### Determines nubmer reads to remove, outputs new ##
######## fq file with correct number of reads ########
######################################################
def downsize_LW_pop():
    directory = lw_ps_directory()

    # use original path
    if len(directory) == 0:
        directory = "/lustre1/mz00685/downsize_read_cov/Run1/"
    remove_lines = directory + "Run1_num_reads.txt"

    #find all LW directories
    fq_directories = glob.glob(directory + "LW*/")

    for lw_dir in fq_directories:

        # All lanes were combined to one fastq for each indiv
        fq= glob.glob(lw_dir + "LW*R1_001.fastq")

        print(fq)

        # Find the individual number
        indiv = fq.split("_")[1]
        reads_to_remove = parse_read_counts(indiv)

        #R1 file downsized
        lw_outputR1 = fq.replace(".fastq", "_ds.fastq")
        fq2 = fq.replace("R1", "R2")
        #R2 file downsized
        lw_outputR2= fq2.replace(".fastq", "_ds.fastq")

        # Open fastq paired files using biopython
        R1 = SeqIO.parse(open(fq), 'fastq')
        R2 = SeqIO.parse(open(fq2), 'fastq')

        # Downsized output
        output1 = open(lw_outputR1, 'w')
        output2 = open(lw_outputR2, 'w')

        print("Read fastq files.")

        seq_identifier = []

        # If more PS reads than LW, don't downsize fq file
        # Append sequence identifiers to array to randomly choose
        # reads for output

        if reads_to_remove > 0:
            for read in R1:

                seq_identifier.append(str(read.id))

            #shuffle array (randomize) and remove reads
            random_seq_identifier = random.shuffle(seq_identifier)
            output_reads = remove_fq_seq(random_seq_identifier, reads_to_remove)

            R1.close()
            R2.close()

            #### Reopen file to pull out the reads for output ####

            R1 = SeqIO.parse(open(fq), 'fastq')
            R2 = SeqIO.parse(open(fq2), 'fastq')

            for read in R1:
                for out in output_reads:
                    if out == str(read.id):
                        output1.write(read.format("fastq"))

            for read in R2:
                for out in output_reads:
                    if out == str(read.id):
                        output2.write(read.format("fastq"))

        else:
            for read in R1:
                output1.write(read.format("fastq"))

            for read in R2:
                output2.write(read.format("fastq"))

        R1.close()
        R2.close()
        output1.close()
        output2.close()
#################################################################################

downsize_LW_pop()
