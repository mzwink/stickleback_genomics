

def calc_avg_cov():

    cov_file = input("Input path to file with average coverage: ")

    output = cov_file.replace("sum.txt", "indiv_sum.txt")
    output = open(output,'w')

    cov_file = open(cov_file).readlines()

    current_indiv = ''
    indiv_sum = 0
    for line in cov_file:
        if line.startswith("LW_"):
            #if not LW_1 - output average


            current_indiv = ''
            indiv_sum = 0

            line = line.split("\t")
            current_indiv = line[0]
            chrom = line[1]
            read_cov = float(line[3])

        else
            line = line.split("\t")
            current_indiv = line[0]
            chrom = line[1]
            read_cov = float(line[3])

            indiv_sum += read_cov
