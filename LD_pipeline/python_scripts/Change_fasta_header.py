 #Converts header line in fasta file from vcf2fasta output to proper sample ID
#Author: Alice Shanfelter August 2016

'''Bash for loop to loop through all fasta files in folder:

for file in *.fasta
do
    python3 Change_fasta_header.py ${file}
done
'''

import fileinput

#Uses the filename to parse out the sample ID and the haplotype number (1 or 2)
#Will need to change name list indeces depending on length of file name
def Change_header():
    haplo_iden = ""
    for line in fileinput.input():
        file = fileinput.filename()
        #split factor will change based on file name
        name = file.split(".")
        whole_iden = name[0]
        #iden should be something like Pop_Ind.No (ex LW_1)
        iden = ''.join(whole_iden[4:len(whole_iden)])
        whole_number = name[1].split(":")
        #No should be the haplotype number right before .fasta, either 0 or 1
        no = whole_number[1]
        #This separates the haplotypes for a single chromosome
        #must do this so that the haplotype configuration file will be correct to create look up table
        if no == '0':
            haplo_iden = '_a'
        elif no == '1':
            haplo_iden = '_b'
        final_header = str(iden) + str(haplo_iden)
    return final_header


#writes all lines from each fasta file with the appropriate header line into one file, no need to use cat *.fasta
#Will need to change output with each chromosome
def write():
    header_line = Change_header()
    with open("PS1B.fasta", 'a') as output:
        for line in fileinput.input():
            if line.startswith(">"):
                output.write('>' + str(header_line) + '\n')
            else:
                output.write(line)

write()
