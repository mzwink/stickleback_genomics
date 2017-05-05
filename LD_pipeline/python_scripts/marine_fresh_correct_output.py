import glob

#Puget sound = population1
#Lake Washington = population2

def correct_output():
    #directory = input("Enter directory of pairwise comparisons: ")

    #making a list of directories
    home_dir="/lustre1/mz00685/LD_pipeline/marine_fresh_populations/pairwise_comp/"
    directories = [home_dir + "fresh_vs_fresh/", home_dir + "marine_vs_fresh/", home_dir + "marine_vs_marine/"]

    for directory in directories:
        if directory.endswith("/") == False:
            directory += "/"
        output_files = glob.glob(directory + "*hotcomp.txt")

        for output in output_files:
            file_name = output.replace(directory, "").replace("_hotcomp.txt", "")
            #example file: Kob_M_Ca_L_chrI_hotcomp.txt
            file_name = file_name.split("_")
            new_output = output.replace(".txt", "_corrected.txt")
            new_output = open(new_output, 'w')
            population1 = file_name[0] + "_" + file_name[1]
            population2 = file_name[2] + "_" + file_name[3]
            chrom = file_name[4]

            output = open(output).readlines()

            for line in output:
                if line.startswith("Hotspot"):
                    line = line.replace("Puget Sound", population1).replace("Lake Washington", population2 + " ")
                    new_output.write(line)
                elif line.startswith("LW"):
                    line = line.replace("LW", population2)
                    new_output.write(line)
                elif line.startswith("PS"):
                    line = line.replace("PS", population1)
                    new_output.write(line)
                else:
                    line = line.replace("PS:", population1+ ":")
                    line = line.replace("LW:", population2 + ":")
                    new_output.write(line)

correct_output()
