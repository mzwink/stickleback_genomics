#Hotspot Overlap between populations
#Hotspots considered overlappingn if within 3kb of another hotspot center
#Author: Alice Shanfelter December 2016

'''
bash code to call script
will need to change based on population being examined
change PS, LW

for file in PS*_hotspots.txt
do
    export in_one=${file}
    export iden=${file%%_*}
    export chr=${iden##*S}
    export in_two=LW${chr}_hotspots.txt
    export output=Chr${chr}_hotcomp.txt
    python3 ~/Documents/UGA/White\ Lab/Project/Scripts/My_scripts/Analysis/Hotspot_Overlap.py
done
'''

import os
#Compares hotspots between populations for a single chromosome
def Compare():
    PSdata = []
    LWdata = []
    PSwindow_center = []
    LWwindow_center = []
    same_hotspots = []
    overlap3kb = []
    in_one = str(os.environ["in_one"])
    in_two = str(os.environ["in_two"])
    out = str(os.environ["output"])
    chr_num = str(os.environ["chr"])
    with open(in_one, 'r') as PSHot, open(in_two, 'r') as LWHot, open(out, 'a') as output:
        for line in PSHot:
            PSdata += line.split()
        PSwindow_start = PSdata[6::3]
        for value in PSwindow_start:
            new_value = int(value)
            new_value = new_value + 1000
            PSwindow_center.append(str(new_value))
        for line in LWHot:
            LWdata += line.split()
        LWwindow_start = LWdata[6::3]
        for value in LWwindow_start:
            new_value = int(value)
            new_value = new_value + 1000
            LWwindow_center.append(str(new_value))
        #will need to change this to proper populations
        output.write("Hotspot Comparison Between Puget Sound and Lake Washington" + str(chr_num)  + '\n' + ("=")*60 + '\n')
        for index, value in enumerate(PSwindow_center):
            if value in LWwindow_center:
                same_hotspots.append(value)
                new_value = '\n' + "Shared Hotspot: " + '\t' + "Center of hotspot: " + value + '\n'
                output.write(new_value)
            elif not value in LWwindow_center:
                low = float(value) - 3000
                high = float(value) + 3000
                for i, val in enumerate(LWwindow_center):
                    if float(val) >= low and float(val) <= high:
                        overlap3kb.append(value)
                        new_value = '\n' + "Overlapping Hotspot by 3kb: " + '\n' + "LW Window Center: " + val + '\n' + "PS Window Center: " + value + '\n'
                        output.write(new_value)
        output.write('\n' + '\n'+ ("=")*50 + '\n' + '\n')
        overlap_less_than_3 = round(((len(same_hotspots) + len(overlap3kb)) / (len(LWwindow_center) + len(PSwindow_center)))*100, 2)
        diff_by_more_than_3 = 100 - overlap_less_than_3
        normalized_data = "Hotspot Analysis" + '\n' + "Number of Hotspots Shared: " + str(len(overlap3kb)) + '\n' + "Percent of Hotspots Shared: " + str(overlap_less_than_3) + '\n' + "Percent of Different Hotspots: " + str(diff_by_more_than_3) + '\n'
        output.write(normalized_data)

Compare()
