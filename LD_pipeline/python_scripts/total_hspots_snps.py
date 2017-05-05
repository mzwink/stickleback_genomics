
populations = ["LW", "PS", "Kob_M", "Ran_M", "Lm_M", "G2_L", "Ca_L", "No_L"]
sample_size = ["10", "15", "20"]
chromosome = ["chrI", "chrII", "chrIII", "chrIV", "chrV", "chrVI", "chrVII", "chrVIII", "chrIX",
"chrX", "chrXI", "chrXII","chrXIII", "chrXIV", "chrXV", "chrXVI", "chrXVII","chrXVIII", "chrXIX",
"chrXX","chrXXI"]

home_directory = "/lustre1/mz00685/LD_pipeline"
pop_info_dict = {"LW20": [home_directory + "/LW_ldpipe/LW20_hotspots/", home_directory + "/population_info/LW/orig_vcf/LW20/"],
"LW15": [home_directory + "/LW_ldpipe/LW15/orig_vcf/hotspots/", home_directory + "/population_info/LW/orig_vcf/LW15/"],
"LW10": [home_directory + "/LW_ldpipe/LW10/orig_vcf/hotspots/", home_directory + "/population_info/LW/orig_vcf/LW10/"],
"PS" : [home_directory + "/PS_ldpipe/orig_vcf/hotspots/", home_directory + "/population_info/PS/"],
"Kob_M" : [home_directory + "/marine_fresh_populations/hotspots/", home_directory + "/population_info/marine_fresh_pop/"],
"Ran_M" : [home_directory + "/marine_fresh_populations/hotspots/", home_directory + "/population_info/marine_fresh_pop/"],
"Lm_M" : [home_directory + "/marine_fresh_populations/hotspots/", home_directory + "/population_info/marine_fresh_pop/"],
"G2_L" : [home_directory + "/marine_fresh_populations/hotspots/", home_directory + "/population_info/marine_fresh_pop/"],
"Ca_L" : [home_directory + "/marine_fresh_populations/hotspots/", home_directory + "/population_info/marine_fresh_pop/"],
"No_L" : [home_directory + "/marine_fresh_populations/hotspots/", home_directory + "/population_info/marine_fresh_pop/"]
}
sample_size_dict = {"Kob_M" : "3", "Ran_M" : "3", "Lm_M" : "6", "G2_L" : "6", "Ca_L" : "6", "No_L" : "6"}

output1 = open("LW_PS_hotspot_snp_summary.txt", 'w')
output2 = open("marine_fresh_snp_summary.txt", 'w')

header = "Population\tSample_Size\tChromosome\tTotal_hotspots\tTotal_Snps\tAverage_Theta\n"
output1.write(header)
output2.write(header)

for p in populations:
    if p == "LW":
        for s in sample_size:
            key = p + s
            hotspot_dir = pop_info_dict[key][0]
            snp_dir = pop_info_dict[key][1]

            for chrom in chromosome:
                #Get first line from hotspot file to get total # hotspots
                hspot_total = open(hotspot_dir + p + "_" + chrom + "_hotspots.txt").readline()
                hspot_total = hspot_total.split(":")[1].rstrip().lstrip()

                snp_total = ''
                avg_theta = ''

                #Parse snp count file for correct chromosome
                snp_file = open(snp_dir + p + s + "_snp_count.txt").readlines()
                theta_file = open(snp_dir + p + s + "_theta.txt").readlines()

                for line in snp_file:
                    line = line.split("\t")
                    curr_chrom = line[1]

                    if curr_chrom == chrom:
                        snp_total  = line[2]
                        snp_total = str(snp_total).rstrip().lstrip()

                pop_chrom = p + "_" + chrom

                for value in theta_file:
                    value = value.split("\t")
                    curr_chrom = value[0]

                    if pop_chrom == curr_chrom:
                        avg_theta = str(value[1]).rstrip().lstrip()


                output1.write(p + "\t" + s + "\t" + chrom + "\t" + hspot_total + "\t" + snp_total +"\t"+ avg_theta +"\n")

    #Population is Puget Sound, sample size == 20
    #If marine/freshwater -> sample size = sample_size_dict[population]

    else:
        if p == "PS":
            s = "20"
        else:
            s = sample_size_dict[p]

        hotspot_dir = pop_info_dict[p][0]
        snp_dir = pop_info_dict[p][1]

        for chrom in chromosome:
            hspot_total = open(hotspot_dir + p + "_" + chrom + "_hotspots.txt").readline()
            hspot_total = hspot_total.split(":")[1].rstrip().lstrip()

            snp_total = ''
            avg_theta = ''

            snp_file = open(snp_dir + p + "_snp_count.txt").readlines()
            theta_file = open(snp_dir + p + "_theta.txt")

            for line in snp_file:
                line = line.split("\t")
                curr_chrom = line[1]

                if curr_chrom == chrom:
                    snp_total  = line[2]
                    snp_total = str(snp_total).rstrip().lstrip()

                pop_chrom = p + "_" + chrom
                for value in theta_file:
                    value = value.split("\t")
                    curr_chrom = value[0]

                    if pop_chrom == curr_chrom:
                        avg_theta = str(value[1]).rstrip().lstrip()


            if p == 'PS':
                output1.write(p + "\t" + s + "\t" + chrom + "\t" + hspot_total + "\t" + snp_total +"\t"+ avg_theta +"\n")
            else:
                output2.write(p + "\t" + s + "\t" + chrom + "\t" + hspot_total + "\t" + snp_total + "\t"+ avg_theta +"\n")
