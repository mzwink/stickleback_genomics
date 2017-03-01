

############### Re-write Fasta ID ##################
### Input: directory to fasta files, populations ###
#####   Output: Fasta file with edited ID's ########
####################################################


from Bio import SeqIO

def edit_fasta_id(directory, population):

    for pop in stickleback_populations:

        pop = pop.replace(" ", "")
        output = open(directory + pop + "_hotspots_con_format.fa", 'w')
        fasta_file = SeqIO.parse(open(directory + pop +'_hotspots_con.fa'), 'fasta')

        counter = 1
        for fasta in fasta_file:

            fasta_header = fasta.id
            fasta_seq = fasta.seq
            fasta_header += '.' + str(counter)
            counter += 1

            output.write(">" + str(fasta_header) + "\n" + str(fasta_seq) + "\n")


############################## Main ##########################

directory = '/Volumes/MW_18TB/Alice_Shanfelter/LakeWashington_PugetSound/MEME/'
stickleback_populations = ["LW", "PS"]

edit_fasta_id(directory, stickleback_populations)
