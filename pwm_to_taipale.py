prdm_genes = ['prdm1a', 'prdm1c', 'prdm2b', 'prdm4', 'prdm8', 'prdm9', 'prdm10', 'prdm12b' ,'prdm13', 'prdm14']

directory = '/Volumes/MW_18TB/Madison_Zwink/stickleback_genome/zinc_finger_motifs/persikov_output/'

for prdm in prdm_genes:
    motif_file = directory + prdm + "_motif_format.txt"

    output = motif_file.replace("_format.txt", ".txt")
    output = open(output, 'w')

    motif_file = open(motif_file).readlines()

    new_header = "\"" + prdm.upper() + " MOTIF\"" + "\n"
    output.write(new_header)

    for value in motif_file:
        value = value.split("  ")

        for info in value:
            info = info.replace("  ", "")
            info = info.replace("\t", "")
            print(info)

            if info.startswith('base') or info.startswith('a') or info.startswith('c') or info.startswith('t') or info.startswith('g'):
                start = info
                start = start.upper()

                new_start = "\"" + start + '\"'

                if start == 'BASE':
                    new_start += "\t" 

                print(new_start)
                output.write(new_start)

            else:
                if info != value[len(value)-1]:
                    output.write(info + "\t")
                else:
                    output.write(info + "\n")
