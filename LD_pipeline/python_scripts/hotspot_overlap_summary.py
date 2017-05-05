
def parse_hotspot_file(hotspot_file, pop1, pop2):

    hspot_shared = ''
    percent_shared_pop2 = ''
    percent_shared_pop1 = ''

    hotspot_values = []
    hotspot_file = open(hotspot_file).readlines()

    for line in hotspot_file:
        if line.startswith("Number of Hotspots Shared"):
            line = line.split(":")
            hspot_shared = str(line[1]).rstrip().lstrip()

        elif line.startswith("Percent of Hotspots Shared in "):
            # + pop2 + ":"):
            line = line.split(":")
            if pop1 in str(line[0]):
                percent_shared_pop1 = str(line[1]).rstrip().lstrip()

            elif pop2 in str(line[0]):
                percent_shared_pop2 = str(line[1]).rstrip().lstrip()



            #percent_shared_pop2 = str(line[1]).rstrip().lstrip()

        #elif line.startswith("Percent of Hotspots Shared in " + pop1 + ":"):
        #    line = line.split(":")
        #    percent_shared_pop1 = str(line[1]).rstrip().lstrip()
#

    hotspot_values = [hspot_shared, percent_shared_pop1, percent_shared_pop2]
    return hotspot_values



populations = ["LW", "PS"] # "Kob_M", "Ran_M", "Lm_M", "No_L", "G2_L", "Ca_L"]
sample_size = ["10", "15", "20"]
chromosome = ["chrI", "chrII", "chrIII", "chrIV", "chrV", "chrVI", "chrVII", "chrVIII", "chrIX",
"chrX", "chrXI", "chrXII","chrXIII", "chrXIV", "chrXV", "chrXVI", "chrXVII","chrXVIII", "chrXIX",
"chrXX","chrXXI"]

home_directory = "/lustre1/mz00685/LD_pipeline/"
LW_LW_comp = home_directory + "LW_LW_pairwise_comp/"
    # LW20_vs_LW15  LW15_vs_LW10  LW20_vs_LW10

LW_PS_comp = home_directory + "LW_PS_pairwise_comp/"
    # PS20_vs_LW10  PS20_vs_LW15  PS20_vs_LW20

output = open("hotspot_overlap_summary.txt", "w")
#Output Format:
# Population1  Population2  Chr  Number hotspots shared   % hotspots in pop1
#           % hotspots in pop2    % unique in pop1  % unique in pop2

header = "Population1\tPopulation2\tChromosome\tNumber_hotspots_shared\tHotspot_overlap_in_population1\tHotspot_overlap_in_population2\n"
output.write(header)


#Loop through for comparisons
pop1 = "LW"
for pop2 in populations:
    i = 0
    j = i + 1

    if pop2 == "LW":
        while j < len(sample_size):
            if pop2 == "LW":
                pop1_sample = sample_size[i]
                pop2_sample = sample_size[j]

                population1 = pop1 + pop1_sample
                population2 = pop2 + pop2_sample

                for chrom in chromosome:
                    #print(pop1 + pop1_sample + "_vs_" + pop2 + pop2_sample + ": " + chrom)
                    hotspot_file = LW_LW_comp + population2 + "_vs_" + population1 + "/orig_vcf/" + population2 + "_" + population1 + "_" + chrom + "_hotcomp.txt"
                    hotspot_values = parse_hotspot_file(hotspot_file, population1 , population2)
                    hspot_shared = hotspot_values[0]
                    percent_shared_pop1 = hotspot_values[1]
                    percent_shared_pop2 = hotspot_values[2]

                    output.write(population1 + "\t" + population2 + "\t" + chrom + "\t" + hspot_shared + "\t" + percent_shared_pop1 + "\t" + percent_shared_pop2 + "\n")


                j += 1
                if j == len(sample_size):
                    i += 1
                    j = i +1


    elif pop2 == "PS":
        while i < len(sample_size):
            pop1_sample = sample_size[i]
            population1 = pop1 + pop1_sample
            population2 = pop2 + "20"

            for chrom in chromosome:
                #print(pop1 + pop1_sample + "_vs_" + pop2 + ": " + chrom)
                hotspot_file = LW_PS_comp + population2  + "_vs_" + population1 + "/orig_vcf/" + population2 + "_" + population1 + "_" + chrom + "_hotcomp.txt"
                hotspot_values = parse_hotspot_file(hotspot_file, population1, population2)

                hspot_shared = hotspot_values[0]
                percent_shared_pop1 = hotspot_values[1]
                percent_shared_pop2 = hotspot_values[2]

                output.write(population1 + "\t" + population2 + "\t" + chrom + "\t" + hspot_shared + "\t" + percent_shared_pop1 + "\t" + percent_shared_pop2 + "\n")

            i += 1


####################################
# Reran hotspot overlap:
#   LW15_vs_LW10
#   LW20_vs_LW15
#   LW20_vs_LW10

#   PS20_vs_LW10
#   PS20_vs_LW15
#   PS20_vs_LW20
