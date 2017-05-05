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

            line = line.split(":")
            if pop1 in str(line[0]):
                percent_shared_pop1 = str(line[1]).rstrip().lstrip()

            elif pop2 in str(line[0]):
                percent_shared_pop2 = str(line[1]).rstrip().lstrip()

    if pop1 == pop2:
        percent_shared_pop2 = percent_shared_pop1

    hotspot_values = [hspot_shared, percent_shared_pop1, percent_shared_pop2]
    return hotspot_values


def compare_populations(pop1_list, pop2_list, directory):

    i = 0
    j = 0
    for pop2 in pop2_list:

        while j < 3 and i < 3:
            pop1 = pop1_list[i]
            pop2 = pop2_list[j]
            print(pop1 + "_" + pop2)

            #print(pop1 + "_" + pop2)
            pop1_sample = sample_size_dict[pop1]
            pop2_sample = sample_size_dict[pop2]

            for chrom in chromosome:
                #print(pop1 + pop1_sample + "_vs_" + pop2 + pop2_sample + ": " + chrom)
                hotspot_file = directory + pop1 + "_" + pop2 + "_" + chrom + "_hotcomp.txt"

                hotspot_values = parse_hotspot_file(hotspot_file, pop1 , pop2)
                hspot_shared = hotspot_values[0]
                percent_shared_pop1 = hotspot_values[1]
                percent_shared_pop2 = hotspot_values[2]

                output.write(pop1 + "\t" + pop2 + "\t" + chrom + "\t" + hspot_shared + "\t" + percent_shared_pop1 + "\t" + percent_shared_pop2 + "\n")

            j += 1
            #print(j)

            if j == 3:
                i += 1
                j = 0



fresh_pop = ["Ca_L" ,"G2_L", "No_L"]
marine_pop = ["Kob_M", "Ran_M", "Lm_M"]
sample_size_dict = {"Kob_M" : "3", "Ran_M" : "3", "Lm_M" : "6", "G2_L" : "6", "Ca_L" : "6", "No_L" : "6"}

chromosome = ["chrI", "chrII", "chrIII", "chrIV", "chrV", "chrVI", "chrVII", "chrVIII", "chrIX",
"chrX", "chrXI", "chrXII","chrXIII", "chrXIV", "chrXV", "chrXVI", "chrXVII","chrXVIII", "chrXIX",
"chrXX","chrXXI"]

home_directory = "/lustre1/mz00685/LD_pipeline/marine_fresh_populations/pairwise_comp/"
marine_marine = home_directory + "marine_vs_marine/"
fresh_fresh = home_directory + "fresh_vs_fresh/"
marine_fresh = home_directory + "marine_vs_fresh/"

output = open("marine_fresh_overlap_summary.txt", "w")
#Output Format:
# Population1  Population2  Chr  Number hotspots shared   % hotspots in pop1
#           % hotspots in pop2

header = "Population1\tPopulation2\tChromosome\tNumber_hotspots_shared\tHotspot_overlap_in_population1\tHotspot_overlap_in_population2\n"
output.write(header)
directories = [marine_marine, fresh_fresh, marine_fresh]

compare_populations(marine_pop, fresh_pop, marine_fresh)
compare_populations(fresh_pop, fresh_pop, fresh_fresh)
compare_populations(marine_pop, marine_pop, marine_marine)
