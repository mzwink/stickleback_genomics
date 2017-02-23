population = ["Ca_L", "Lm_M", "Kob_M", "Ran_M", "Lm_M", "No_L", "G2_L"]
chromosomes = ["chrXXI", "chrXX", "chrXIX", "chrXVIII", "chrXVII", "chrXVI", "chrXV", "chrXIV", "chrXIII", "chrXII",
"chrXI", "chrX", "chrIX", "chrVIII", "chrVII","chrVI", "chrV", "chrIV", "chrIII", "chrII", "chrI"]

directory='/lustre1/mz00685/LD_pipeline/fasta_files/chromosome_fasta/'
new_directory='/lustre1/mz00685/LD_pipeline/vcf/phased_vcf/sites/'
for pop in population:
    for chrom in chromosomes:
        fasta_file = directory + pop + "_" + chrom + ".fasta"

        print(fasta_file)
        fasta_file = open(fasta_file).readlines()

        output = open(new_directory + pop + "_" + chrom + "_sites.txt", "w")


        for line in fasta_file:
            line = line.rstrip()
            if line.startswith(">"):
                output.write("\n" +line + "\n")

            else:
                output.write(line)

        #if line == fasta_file[len(fasta_file)-1]:
        #    print("Print to output 2")
        #    output.write(fasta_id + "\n")
        #    output.write(fasta_seq + "\n")
