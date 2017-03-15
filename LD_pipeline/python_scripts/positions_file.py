directory = '/Volumes/MW_18TB/Alice_Shanfelter/LakeWashington_PugetSound/MEME/Madison_Output/phased_vcf/'

population = ["Ca_L", "Lm_M", "Kob_M", "Ran_M", "Lm_M", "No_L", "G2_L"]
chromosomes = ["chrXXI", "chrXX", "chrXIX", "chrXVIII", "chrXVII", "chrXVI", "chrXV", "chrXIV", "chrXIII", "chrXII",
"chrXI", "chrX", "chrIX", "chrVIII", "chrVII","chrVI", "chrV", "chrIV", "chrIII", "chrII", "chrI"]


for pop in population:
    for chrom in chromosomes:

        vcf_file = directory+ pop + "_jG_" +chrom + "_phased.vcf"
        output = directory+ pop+"_" + chrom + "_pos.txt"
        vcf_file = open(vcf_file).readlines()
        output = open(output, 'w')

        for line in vcf_file:
            if line.startswith("#") == False:
                line = line.split("\t")

                pos=line[1]

                output.write(pos + "\n")
